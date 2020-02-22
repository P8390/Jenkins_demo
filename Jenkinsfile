pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                retry(2) {
                echo 'In Build Stage'
                }
                timeout(time:3, unit:'SECONDS') {
                    sleep(5)
                    echo 'Hey, In Timeout!!'
                }
            }
        }
        stage('run') {
            steps {
                echo 'In Running Stage'
                sh 'python hello_workd.py'
            }
        }
    }
}
