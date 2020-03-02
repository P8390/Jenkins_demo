pipeline {
  agent any
  stages {
    stage('Build Env') {
      steps {
        git(branch: 'master', credentialsId:'b0478fef-b98a-4c7c-8935-5d5ffc68b131', url: 'https://github.com/P8390/Jenkins_demo.git')
        echo 'inside of build stage'
      }
    }
    post {
      always {
        echo 'run successfully'
      }
    }
  }
}
