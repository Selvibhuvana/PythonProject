#ProjectName : simple ETL test cases automation

#Demo
File ETL_test_suite.robot is written in SQL using Python's Robot Framework checking basic table checks. 
File ETL_mutation_test_suite.robot is the file checking idempotency and incremental check
Tables are created in snowflake and snowflake is connected to Robot Framework and  through Snowflake ODBC driver
Jenkinsfile is pointed to snowflake odbc and connection passwords are included in JenkinsCredentials

Once after performing all the above . The scripts can be run with Jenkins --> Build with Parameters --> point to Snowflake --> Run. 
The resultant robot framework files [log, report and Output] will provide all the details on the test cases.

