pipeline {
  agent { docker { image 'python:3.5.1' } }
  stages {
    stage ('build') {
      steps {
        sh '''/usr/local/bin/virtualenv jenkins_demo
        source jenkins_demo/bin/activate
        /Users/pankaj/.jenkins/workspace/multi_master/jenkins_demo/bin/pip install -r requirements.txt
        '''
      }
    }
    stage ('test') {
      steps {
        sh ''' source jenkins_demo/bin/activate 
          python app.py
          python tests.py
        '''
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }

}
