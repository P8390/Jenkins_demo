pipeline {
  agent any
  stages {
    stage ('build') {
      steps {
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
