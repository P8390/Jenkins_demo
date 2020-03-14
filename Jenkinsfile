
pipeline {
  agent any
  environment {
    CREDENTIAL = credentials('0d7e3a4c-8fcf-4ff9-b72b-a3154118a288')
    GIT_USERNAME = "${env.CREDENTIAL_USR}"
    GIT_PASSWORD = "${env.CREDENTIAL_PSW}"
  }
  stages {
    stage('Build') {
      steps {
        git(branch: 'master', credentialsId: '0d7e3a4c-8fcf-4ff9-b72b-a3154118a288', url: 'https://github.com/P8390/Jenkins_demo.git')
        sh 'ls -lat'
        withCredentials([usernamePassword(credentialsId: '0d7e3a4c-8fcf-4ff9-b72b-a3154118a288', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]){
        echo 'inside the ..'
          echo $GIT_USERNAME
          echo $GIT_PASSWORD
        }
      }
    }
  }
}
