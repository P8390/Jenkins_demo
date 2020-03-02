pipeline {
  agent any
  stages {
    stage('Build Env') {
      steps {
        git(branch: 'master', credentialsId:'b0478fef-b98a-4c7c-8935-5d5ffc68b131', url: 'https://github.com/P8390/Jenkins_demo.git')
        withCredentials(bindings: [usernamePassword(credentialsId: '4dcba0e4-027c-4edb-b9f3-909bfe955215', usernameVariable: 'username', passwordVariable: 'password')]){
        sh 'echo $username'
        sh 'echo $password'
        }
      }
    }
  }
}
