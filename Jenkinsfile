pipeline {
  agent any
  stages {
    stage('Initialize') {
      parallel {
        stage('Initialize') {
          steps {
            echo 'Pipeline starting'
          }
        }
        stage('error') {
          steps {
            echo 'Multibrach Pipeline starting'
          }
        }
      }
    }
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test') {
      steps {
        build 'codewarrior'
      }
    }
    stage('deploy') {
      steps {
        echo 'Pipeline completed'
      }
    }
  }
}