pipeline {
  agent any
 
  stages {
    stage('Init') {
      steps {
        sh 'python3 -m venv venv && venv/bin/pip install -r requirements.txt'
     
        python3 rds-automation.py
      }
    }
  }
}