
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
        sh '''
          ls -lat
          TARBALL=`tar -zcf demo_deploy.tgz .`
          echo "tar errors = $TARBALL , blank if none"
        '''
      }
    }
    post {
      success {
        archiveArtifacts(onlyIfSuccessful: true, artifacts: '*_deploy.tgz', fingerprint: true)
      }
      failure {
                cleanWs()
            }
    }
  }
}
