pipeline {
  agent any
 
  stages {
    stage('Init') {
      steps {
        withAWS(credentials: 'newt-aws', region: 'us-east-1') {      
          sh '''
            payload='{"key1": "value1", 
                      "key2": "value2", 
                      "key3": "value3"}'
            output=$(aws lambda invoke --function-name 'testfunction' --payload "$payload"  output.json --cli-binary-format raw-in-base64-out)
            echo "$output"
          '''
        }
      }
    }
  }
}