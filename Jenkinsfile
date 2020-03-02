pipeline {
  agent any
  stages {
    stage('Build Env') {
      steps {
        git(branch: 'master', credentialsId:'4dcba0e4-027c-4edb-b9f3-909bfe955215', url: 'https://github.com/P8390/Jenkins_demo.git')
        withCredentials(bindings: [usernamePassword(credentialsId: '4dcba0e4-027c-4edb-b9f3-909bfe955215', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]){
        echo $GIT_USERNAME
        echo $GIT_PASSWORD
        }
      }
    }
  }
}
