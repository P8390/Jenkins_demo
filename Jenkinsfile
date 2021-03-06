
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
            sh 'sonar-scanner -Dsonar.token=bef0a6010c354aeb771b0b2a414391b102ed0ffb -Dsonar.projectKey=$project_key -Dsonar.sources=. -DfailIfNoTests=true -Dsonar.scm.provider=git  -Dsonar.exclusions=*.xml -Dsonar.exclusions=*_env/**/* -Dsonar.test.exclusions=*test*/*,./*.xml -Dsonar.python.xunit.reportPath=nosetests.xml  -Dsonar.core.codeCoveragePlugin=cobertura -Dsonar.python.coverage.reportPaths=coverage.xml'
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
          timeout(time:1, unit: 'MINUTES'){
            withSonarQubeEnv('sonarqube'){
             sleep(10)
             waitForQualityGate abortPipeline: true
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
          withEnv(overrides:["project_key=${PROJECT}"]){
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
        stage('Promotion') {
          when {
          anyOf {
            branch 'integration'
            branch 'staging'
            branch 'master'
          }
        }
          post {
            always {
              cleanWs()
              mail to: 'pankaj@screen-magic.com',
                subject: "Jenkins Build ${env.JOB_NAME} #${env.BUILD_NUMBER} Awaits Approval",
                body: "The ${BRANCH_NAME} build is ready to be promoted.\n\nConsole: ${env.BUILD_URL}.\n\n"
            }
          }
          steps {
            timeout(time: 60, unit: 'SECONDS'){
              input 'sanity before production. okay ?'
            }
          }
        }
        stage('Deploy') {
          when {
            anyOf {
                branch 'integration'
                branch 'staging'
                branch 'master'
                }
            }
          steps {
            git(branch: "${BRANCH_NAME}", credentialsId: '0d7e3a4c-8fcf-4ff9-b72b-a3154118a288', url: 'https://github.com/P8390/Jenkins_demo.git')
            unarchive(mapping: ['*_deploy*': '.'])
            withEnv(overrides: ["project_key=${PROJECT}", "enviornment_key=${BRANCH_NAME}"]){
              ansiblePlaybook(
                              inventory: 'ansible_hosts',
                              playbook: 'ansible_playbook.yml',
                              colorized: true
                            )
            }
          }
          post {
            always {
                cleanWs()
              mail to: 'pankaj@screen-magic.com',
             subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
             body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
            }
        }
        }
      }
    }
