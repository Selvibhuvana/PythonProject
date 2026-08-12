pipeline {
    agent any
    parameters {
        choice(name: 'DATABASE_TARGET', choices: ['LOCAL', 'SNOWFLAKE'],
               description: 'Which warehouse to validate against')
    }
    stages {
        stage('Run ETL Tests') {
            steps {
                script {
                    if (params.DATABASE_TARGET == 'SNOWFLAKE') {
                        withCredentials([string(credentialsId: 'ETL_SF_PASSWORD', variable: 'SF_PWD')]) {
                            dir('robot tests') {
                                bat 'C:/Users/selvi/AppData/Local/Programs/Python/Python314/Scripts/robot.exe --variable ODBC_DRIVER:SnowflakeDSIIDriver --variable DB_SERVER:ewc30549.us-east-1.snowflakecomputing.com --variable DB_NAME:ETL_LAB --variable DB_USER:robot_tester --variable DB_PASSWORD:%SF_PWD% --outputdir results_sf ETL_test_suite.robot ETL_mutation_test_suite.robot'
                            }
                        }
                    } else {
                        withCredentials([string(credentialsId: 'ETL_DB_PASSWORD', variable: 'DB_PWD')]) {
                            dir('robot tests') {
                                bat 'C:/Users/selvi/AppData/Local/Programs/Python/Python314/Scripts/robot.exe --variable DB_PASSWORD:%DB_PWD% --outputdir results ETL_test_suite.robot'
                            }
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                def rd = params.DATABASE_TARGET == 'SNOWFLAKE' ? 'robot tests/results_sf' : 'robot tests/results'
                step([$class: 'RobotPublisher',
                      outputPath: rd,
                      outputFileName: 'output.xml',
                      reportFileName: 'report.html',
                      logFileName: 'log.html',
                      passThreshold: 90.0,
                      unstableThreshold: 70.0])
                archiveArtifacts artifacts: "$rd/*", allowEmptyArchive: true
            }
        }
    }
}