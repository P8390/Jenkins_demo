pipeline {
  agent any
  stages {
    stage ('build') {
      steps {
        sh 'virtualenv jenkins_demo'
        sh 'source jenkins_demo/bin/activate'
        sh '/usr/local/bin/pip install -r requirements.txt'
      }
    }
    stage ('test') {
      steps {
        sh 'python tests.py'
      }
    }
  }

}
