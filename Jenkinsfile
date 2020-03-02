pipeline {
  agent any
  stages {
    stage('Build Env') {
      steps {
        echo 'inside of build stage'
      }
    }
  }
    post {
      always {
        echo 'run successfully'
      }
    }
}
