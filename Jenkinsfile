pipeline {
    agent any

    stages {
        stage('Run ETL Tests') {
            steps {
                dir('robot tests') {
                    bat 'C:/Users/selvi/AppData/Local/Programs/Python/Python314/Scripts/robot.exe --outputdir results ETL_test_suite.robot'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'robot tests/results/*', allowEmptyArchive: true
        }
    }
}