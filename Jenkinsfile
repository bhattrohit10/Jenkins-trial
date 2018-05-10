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
        stage('') {
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
        archiveArtifacts 'new'
      }
    }
  }
}