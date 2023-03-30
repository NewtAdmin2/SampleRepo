pipeline {
  agent any
   parameters {
        string(name: "CUSTOM_USERNAME", defaultValue: "", trim: true, description: "User to be added into RDS")
        string(name: "DATABASE", defaultValue: "", trim: true, description: "Target database where user to be added")
        string(name: "RDS_HOST", defaultValue: "", description: "Target RDS instance")
        choice(name: "ACTION", choices: ["Add", "Remove"], description: "Action to be performed on RDS")
    }
  stages {
    stage('Init') {
      steps {
        withAWS(credentials: 'newt-aws', region: 'us-east-1') {      
          sh '''
            // payload='{"key1": "value1", 
            //           "key2": "value2", 
            //           "key3": "value3"}'
            // output=$(aws lambda invoke --function-name 'testfunction' --payload "$payload"  output.json --cli-binary-format raw-in-base64-out)
            // echo "$output"

            echo "custom username: $params.CUSTOM_USERNAME"
            echo "custom DATABASE: $params.DATABASE"
            echo "custom RDS_HOST: $params.RDS_HOST"
            echo "custom ACTION: $params.ACTION"

            python3 rds-full-automation.py

          '''
        }
      }
    }
  }
}