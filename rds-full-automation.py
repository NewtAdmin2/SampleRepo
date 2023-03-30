import boto3
import json
import random
import string
import os

print(os.environ['CUSTOM_USERNAME'])
print(os.environ['DATABASE'])
print(os.environ['RDS_HOST'])
print(os.environ['ACTION'])

# # create a Secrets Manager client
# secret_client = boto3.client('secretsmanager',region_name='us-east-1')

# #Create random password
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for i in range(10))
# print("Random password is:", password)

# custom_user_name = 'testuser25'
# custom_user_pwd = password
# database_name = 'database1'
# rds_host = 'arn:aws:rds:us-east-1:401545458111:cluster:database-1'

# ##Step 1: create secret for custom user
# create_secret_response = secret_client.create_secret(Name="8", Description="User secret store for RDS",
#                                             SecretString=json.dumps({"username": custom_user_name,"password":password}))

# print(create_secret_response["ARN"])

# #Step 2: Get master creds from secret store
# response = secret_client.get_secret_value(SecretId='rds!cluster-ea6cf62c-e20c-4d81-80f7-8e645696e31e')

# # if the secret is a string, return it directly
# if 'SecretString' in response:
#     print(response['SecretString'])
#     secret = json.loads(response['SecretString'])
# else:
#     binary_secret_data = response['SecretBinary']
#     decoded_secret = base64.b64decode(binary_secret_data)
#     print(decoded_secret)

# #Step 3: Invoke lambda api
# lambda_client = boto3.client('lambda')
# lambda_payload = {"name": "name","age":"age"}
                    
# lambda_response = lambda_client.invoke(FunctionName='testfunction', 
#                     InvocationType='RequestResponse',
#                     Payload=json.dumps({"username": custom_user_name,"password":password}))

# print(lambda_response['Payload'].read())
