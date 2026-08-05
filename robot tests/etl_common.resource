*** Settings ***
Library    DatabaseLibrary

*** Variables ***
${ODBC_DRIVER}    {ODBC Driver 17 for SQL Server}
${DB_SERVER}      localhost\\SQLEXPRESS
${DB_NAME}        msdb
${DB_USER}        etl_tester

*** Keywords ***
Connect To ETL Database
        Connect To Database    pyodbc    odbc_driver=${ODBC_DRIVER}    server=${DB_SERVER}    database=${DB_NAME}    db_user=${DB_USER}    db_password=${DB_PASSWORD}
