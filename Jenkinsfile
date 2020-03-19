
pipeline {
  agent any
  environment {
    CREDENTIAL = credentials('0d7e3a4c-8fcf-4ff9-b72b-a3154118a288')
    GIT_USERNAME = "${env.CREDENTIAL_USR}"
    GIT_PASSWORD = "${env.CREDENTIAL_PSW}"
    PROJECT = 'Jenkins_demo'
    PYTHONPATH = "${WORKSPACE}"
  }
  stages {
    stage('Build Env') {
      steps {
        git(branch: "${BRANCH_NAME}", credentialsId: '0d7e3a4c-8fcf-4ff9-b72b-a3154118a288', url: 'https://github.com/P8390/Jenkins_demo.git')
        sh 'ls -lat'
          withEnv(overrides: ["project_key=${PROJECT}"]){
            sh '''
              pip3 install virtualenv
              virtualenv -p python3 "$project_key"_env
              source "$project_key"_env/bin/activate
              pip install -r requirements.txt --no-cache-dir
              TARBALL=`tar --exclude=\'"$project_key"_deploy.tgz\' --exclude=\'.git\' -zcf "$project_key"_deploy.tgz . `
            '''
          }
        }
    post{
      success {
        archiveArtifacts(onlyIfSuccessful: true, artifacts: '*_deploy.tgz', fingerprint: true)
      }
      failure {
         cleanWs()
      }
     }
    }
   stage('Run Tests') {
      when {
        anyOf {
          branch 'integration'
          branch 'staging'
          branch 'master'
        }
      }
      steps {
        withEnv(overrides:["project_key=${PROJECT}", "enviornment_key=${BRANCH_NAME}"]){
          sh '''
            source "$project_key"_env/bin/activate
            python --version
            pip freeze
            nosetests unittests --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-xml --cover-xml-file=coverage.xml  --cover-package main_app || echo export RESULT=failures
          '''
          junit 'nosetests.xml'          
          cobertura coberturaReportFile: 'coverage.xml'          
        }
      }
    }
    stage('Quality Check') {
      when {
        anyOf {
          branch 'integration'
          branch 'staging'
          branch 'master'
        }
      }
      steps {
        withEnv(overrides:["project_key=${PROJECT}"]){
          withSonarQubeEnv('sonarqube'){
            sh 'sonar-scanner -Dsonar.login=admin -Dsonar.password=admin -Dsonar.projectKey=$project_key -Dsonar.sources=. -DfailIfNoTests=true -Dsonar.scm.provider=git -Dsonar.exclusions=*_env/**/* -Dsonar.test.exclusions=*test*/*,./*.xml -Dsonar.python.xunit.reportPath=nosetests.xml  -Dsonar.core.codeCoveragePlugin=cobertura -Dsonar.python.coverage.reportPaths=coverage.xml'
          }
        }
      }
    }
     stage('Quality Gate') {
        when {
          anyOf {
            branch 'integration'
            branch 'staging'
            branch 'master'
          }
        }
        steps {
          timeout(time:15, unit: 'MINUTES'){
            withSonarQubeEnv('sonarqube'){
              waitForQualityGate true
            }
          }
        }
     }
      stage('Test Result') {
        when {
          anyOf {
            branch 'integration'
            branch 'staging'
            branch 'master'
          }
        }
        steps {
          sh '''
            source "$project_key"_env/bin/activate
            echo "Test result - $RESULT"
            if [ "$RESULT" = failures ]
                then
                   exit 1
                  #exit 0                     #=======Dry run always success==========
            fi
          '''
        }
      }
    }
  }
