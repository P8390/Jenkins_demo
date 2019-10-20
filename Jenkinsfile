pipeline {
    agent {
        docker 
          { image 'python:2.7' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
