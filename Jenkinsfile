pipeline {
  agent any
  stages {
    stage('build') {
      #steps {
      #  sh 'pip install -r requirements.txt'
      #}
    }
    stage('test') {
      steps {
        sh 'python --version'
      }
      post {
        always {
      #    junit 'test-reports/*.xml'
        }
      }
    }
  }
}
