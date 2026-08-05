pipeline {
    agent any

        stage('Run ETL Tests') {
            steps {
                withCredentials([string(credentialsId: 'ETL_DB_PASSWORD', variable: 'DB_PASSWORD')]) {
                    dir('robot tests') {
                        bat 'C:/Users/selvi/AppData/Local/Programs/Python/Python314/Scripts/robot.exe --variable DB_PASSWORD:%DB_PASSWORD% --outputdir results ETL_test_suite.robot'
                    }
                }
            }
        }

    post {
        always {
			step([$class: 'RobotPublisher',
                  outputPath: 'robot tests/results',
                  outputFileName: 'output.xml',
                  reportFileName: 'report.html',
                  logFileName: 'log.html',
                  passThreshold: 90.0,
                  unstableThreshold: 70.0])
            archiveArtifacts artifacts: 'robot tests/results/*', allowEmptyArchive: true
        }
    }
}