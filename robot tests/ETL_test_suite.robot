*** Settings ***
Documentation    Full ETL test suite exercise
Resource    etl_common.resource
#Library    DatabaseLibrary   --- this is not needed because resource will automatically import it.
Library    String    # adding this for loop function in transformation test
Suite Setup    Connect To ETL Database
Suite Teardown    Disconnect From Database

*** Test Cases ***
Table Count Validation
    ${allcnts}=    Query      select * from (select 'stg.Raw_Customer' as table_name,count(*) as Counts from stg.Raw_Customer union select 'stg.Raw_Transactions' as table_name,count(*) as Counts from stg.Raw_Transactions union select 'dw.Dim_Customer' as table_name,count(*) as Counts from dw.Dim_Customer union select 'dw.Fact_Transactions' as table_name,count(*) as Counts from dw.Fact_Transactions)z order by table_name
    #ordering br table_name in alphabetical order so count will match as expected
    Should Be Equal As Numbers    ${allcnts[0][1]}    3
    Should Be Equal As Numbers    ${allcnts[1][1]}    4
    Should Be Equal As Numbers    ${allcnts[2][1]}    4
    Should Be Equal As Numbers    ${allcnts[3][1]}    4

No Missing rows
    Check Row Count   select * from stg.Raw_Transactions src join dw.Fact_Transactions tgt on src.txn_id = tgt.transaction_id    ==    4
    Check Row Count   select * from stg.Raw_Transactions src left join dw.Fact_Transactions tgt on src.txn_id = tgt.transaction_id where tgt.transaction_id is null    ==    0
    Check Row Count    select * from dw.Fact_Transactions tgt left join stg.Raw_Transactions src on src.txn_id = tgt.transaction_id where src.txn_id is null    ==    0
    
No Missing rows - NOT EXISTS
    Check Row Count    select * from stg.Raw_Transactions src where not exists (select * from dw.Fact_Transactions tgt where src.txn_id = tgt.transaction_id)    ==    0
    Check Row Count    select * from dw.Fact_Transactions tgt where not exists (select * from stg.Raw_Transactions src where src.txn_id = tgt.transaction_id )    ==    0
Only valid records passed thru
    Check Row Count   select * from stg.Raw_Customer where account_status in ('ACTIVE','INACTIVE') and stg_cust_id not in (select source_customer_id from dw.Dim_customer)    ==    0

Name check
    ${rows}    Query    Select RC.first_name,RC.last_name,DC.full_name from stg.Raw_Customer RC join dw.Dim_Customer DC on RC.stg_cust_id = DC.source_customer_id;
    FOR     ${row}     IN      @{rows}
        ${expected}    Convert to Uppercase     ${row[0]} ${row[1]}    # space is to be provided as the 1st and last name is concatenated with a space
        Should Be Equal    ${row[2]}          ${expected}
    END
Active check
    Check Row Count    Select * from (select tgt.is_active,case when src.account_status='ACTIVE' then 1 else 0 end as src_is_active from stg.Raw_Customer src join dw.Dim_Customer tgt on src.stg_cust_id = tgt.source_customer_id)a where is_active!=src_is_active    ==    0

Active check - Python style
    ${rows}    Query    SELECT d.is_active, s.account_status FROM dw.Dim_Customer d JOIN stg.Raw_Customer s ON d.source_customer_id = s.stg_cust_id
    FOR    ${row}    IN    @{rows}
        ${expected}    Evaluate    '${row[1]}' == 'ACTIVE'            # here quites is important around the variable because only then it will  be compared with string
        Should Be Equal    ${row[0]}    ${expected}
    END

Date checks customer
    Check Row Count    select * from (Select cast(src.created_date as date)as src_date,tgt.created_date from stg.Raw_Customer src join dw.Dim_Customer tgt on src.stg_cust_id = tgt.source_customer_id )a where src_date!=created_date    ==    0
Date checks transactions
    Check Row Count    select * from (Select cast(src.txn_date as datetime)as src_date,tgt.transaction_date from stg.Raw_Transactions src join dw.Fact_Transactions tgt on src.txn_id = tgt.transaction_id)a where src_date!=transaction_date    ==    0
Amount datatype check
    Check Row Count    select * from (Select cast(src.txn_amount as number(18,2)) as src_amount,tgt.amount from stg.Raw_Transactions src join dw.Fact_Transactions tgt on src.txn_id = tgt.transaction_id)a where src_amount!=amount    ==    0
    
Surrogate key check
    Check Row Count    select * from dw.Fact_Transactions tgt join stg.Raw_Transactions src on src.txn_id=tgt.transaction_id join dw.Dim_customer DC on DC.customer_key = tgt.customer_key and src.stg_cust_id!=DC.source_customer_id    ==    0
Bad record exclusion
    Check Row Count    select * from stg.raw_customer src where account_status = 'PENDING' and exists (select * from dw.Dim_customer tgt where tgt.source_customer_id = src.stg_cust_id)    ==    0
    
NULL checks 
    Check Row Count    select * from dw.Dim_customer where (customer_key is null or source_customer_id is null or full_name is null or is_active is null or created_date is null)    ==    0
    Check Row Count    select * from dw.Fact_transactions where (fact_txn_id is null or transaction_id is null or amount is null or transaction_type is null or transaction_date is null)    ==    0

Duplicate checks
    Check Row Count    select customer_key,count(*) from dw.Dim_customer group by customer_key having count(*) >1    ==    0
    Check Row Count    select transaction_id,count(*) from dw.Fact_transactions group by transaction_id having count(*)>1    ==    0
    
Non Existent customer Key
    Check Row Count    select * from dw.Fact_transactions tgt left join dw.Dim_customer src on src.customer_key = tgt.customer_key where src.customer_key is null    ==    0
    
    


