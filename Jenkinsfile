pipeline {
  agent any
 
  stages {
    stage('Init') {
      steps {
        withAWS(credentials: 'newt-aws', region: 'us-east-1') {      
          sh '''
            python3 -m venv venv && venv/bin/pip install -r requirements.txt

            venv/bin/pip install pymysql
        
            python3 rds-automation.py
          '''
        }
      }
    }
  }
}