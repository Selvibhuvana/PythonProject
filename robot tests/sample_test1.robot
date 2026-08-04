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
ETL Database Is Reachable
    [Tags]    smoke
    ${source_rows}    Row Count    SELECT COUNT(*) FROM stg.Raw_Customer
    Log    Source table stg.Raw_Customer has ${source_rows} rows.
    Should Be True    ${source_rows} > 0    Source table should not be empty