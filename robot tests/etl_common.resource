*** Settings ***
Library    DatabaseLibrary

*** Variables ***
${ODBC_DRIVER}    {ODBC Driver 17 for SQL Server}
${DB_SERVER}      localhost\\SQLEXPRESS
${DB_NAME}        msdb

*** Keywords ***
Connect To ETL Database
    Connect To Database    pyodbc    odbc_driver=${ODBC_DRIVER}    server=${DB_SERVER}    database=${DB_NAME}    trusted_connection=yes
