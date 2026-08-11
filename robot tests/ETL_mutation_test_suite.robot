*** Settings ***
Documentation    Mutation ETL test suite exercise
Resource    etl_common.resource
#Library    DatabaseLibrary   --- this is not needed because resource will automatically import it.
Library    String    # adding this for loop function in transformation test
Suite Setup    Connect To ETL Database
Suite Teardown    Disconnect From Database


*** Test Cases ***
Deleting mock data in each iteration from tgt
    Execute Sql String     Delete from dw.Dim_Customer where source_customer_id = 'CUST-1005'
    Execute Sql String     Delete from dw.Fact_Transactions where transaction_id = 'TXN-8005'
Deleting mock data in each iteration from stg and insert incremental data - Customer
    Execute Sql String     Delete from stg.Raw_Customer where stg_cust_id = 'CUST-1005';
    Execute Sql String     INSERT INTO stg.Raw_Customer VALUES ('CUST-1005','david','brown','david@example.com','ACTIVE','2025-04-01')
Deleting mock data in each iteration from stg and insert incremental data - Transaction
    Execute Sql String     Delete from stg.Raw_Transactions where txn_id = 'TXN-8005'
    Execute Sql string     INSERT INTO stg.Raw_Transactions VALUES('TXN-8005','CUST-1005','99.99','DEPOSIT','2026-07-10 08:00:00');
Checking counts post mock data insertion into Stg
    Check row count        select * from stg.Raw_Customer    ==    5
    Check Row Count       select * from stg.Raw_transactions    ==    5
Executing task to see incremental insertion in tgts
    Execute Sql String    EXECUTE TASK ETL_LAB.PUBLIC.ETL_LOAD_STG_TO_DW;
    Wait Until Keyword Succeeds    1 min    20 sec    Check Row Count       select * from dw.Dim_Customer    ==    4
    Check Row Count       select * from dw.Fact_Transactions    ==    5
Executing twice to check idempotency
    Execute Sql String    EXECUTE TASK ETL_LAB.PUBLIC.ETL_LOAD_STG_TO_DW;
    Wait Until Keyword Succeeds    1 min    20 sec    Check Row Count       select * from dw.Dim_Customer    ==    4
    Check Row Count       select * from dw.Fact_Transactions    ==    5
Mock data cleanup
    Execute Sql String    Delete from stg.Raw_Customer where stg_cust_id = 'CUST-1005';
    Execute Sql String    Delete from stg.Raw_Transactions where txn_id = 'TXN-8005'
    Execute Sql String    Delete from dw.Dim_Customer where source_customer_id = 'CUST-1005'
    Execute Sql String    Delete from dw.Fact_Transactions where transaction_id = 'TXN-8005'
Checking counts after cleanup
    Check row count        select * from stg.Raw_Customer    ==    4
    Check Row Count       select * from stg.Raw_transactions    ==    4
    Check Row Count       select * from dw.Dim_Customer    ==    3
    Check Row Count       select * from dw.Fact_Transactions    ==    4




