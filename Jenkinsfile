pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'In Build Stage'
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
