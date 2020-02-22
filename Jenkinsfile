pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                retry(2) {
                sh 'In Build Stage'
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
