pipeline {
  agent any
  stages {
    stage ('build') {
      steps {
        sh '''/usr/local/bin/virtualenv jenkins_demo
        source jenkins_demo/bin/activate
        /usr/local/bin/pip install -r requirements.txt
        /usr/local/bin/pip freeze
        '''
      }
    }
    stage ('test') {
      steps {
        sh ''' source jenkins_demo/bin/activate 
          python tests.py
        '''
      }
    }
  }

}
