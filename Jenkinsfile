pipeline {
    agent any
    environment {
        AUTH = 'oauth2'
        DB_ENGINE = 'Mysql'
    }
    stages {
        stage('build') {
            steps {
                retry(2) {
                echo 'In Build Stage'
                }
                timeout(time:3, unit:'SECONDS') {
                    echo 'Hey, In Timeout!!'
                }
                echo "AUTH for this project - ${AUTH}"
                echo "DB ENGINE - ${DB_ENGINE}"
            }
        }
        stage('run') {
            steps {
                echo 'In Running Stage'
                sh 'python hello_workd.py'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only only if successful'
        }
        failure {
            echo 'In case of failure'
        }
        unstable {
            echo 'if unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
