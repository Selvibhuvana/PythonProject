*** Settings ***
Documentation    My first ETL test - verify we can talk to the warehouse database.
Library          DatabaseLibrary
Suite Setup      Connect To Database    pyodbc    odbc_driver=${ODBC_DRIVER}    server=${DB_SERVER}    database=${DB_NAME}    trusted_connection=yes
Suite Teardown   Disconnect From Database
*** Variables ***
${ODBC_DRIVER}    {ODBC Driver 17 for SQL Server}
${DB_SERVER}      localhost\\SQLEXPRESS
${DB_NAME}        msdb
*** Test Cases ***
Checking row count
    ${count}=    Check Row Count    SELECT * FROM dw.Fact_Transactions    ==    4
Checking amount details
    ${row}=      Query    select * from dw.Fact_Transactions where transaction_id = 'TXN-8001'
    Should Be Equal As Numbers    ${row[0][3]}    250.50
    Should Be Equal               ${row[0][4]}    DEPOSIT
Checking bad data
    ${badcount}=    Check Row Count    SELECT * FROM dw.Dim_Customer where source_customer_id ='CUST-1004'        ==       0