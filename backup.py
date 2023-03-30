import boto3
import pymysql
import json
import random
import string

# create a Secrets Manager client
client = boto3.client('secretsmanager',region_name='us-east-1')

#Create random password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(10))
print("Random password is:", password)

custom_user_name = 'testuser25'
custom_user_pwd = password
database_name = 'database1'
rds_host = 'arn:aws:rds:us-east-1:401545458111:cluster:database-1'

# Step 1: create secret for custom user
# create_secret_response = client.create_secret(Name="8", Description="User secret store for RDS",
#                                               SecretString=json.dumps({"username": custom_user_name,"password":password}))

# # custom_secret_arn= json.loads(create_secret_response['ARN'])
# print(create_secret_response["ARN"])

#step 2: Get master creds from secret store
response = client.get_secret_value(SecretId='rds!cluster-ea6cf62c-e20c-4d81-80f7-8e645696e31e')
# secret = ''

# if the secret is a string, return it directly
if 'SecretString' in response:
    print(response['SecretString'])
    secret = json.loads(response['SecretString'])

# if the secret is binary, decode it using base64
else:
    binary_secret_data = response['SecretBinary']
    decoded_secret = base64.b64decode(binary_secret_data)
    print(decoded_secret)
#Step 3: Invoke lambda api
lambda_client = boto3.client('lambda')
lambda_payload = {"name": "name","age":"age"}
                    
lambda_response = lambda_client.invoke(FunctionName='testfunction', 
                     InvocationType='RequestResponse',
                     Payload=json.dumps({"username": custom_user_name,"password":password}))

print(lambda_response['Payload'].read())

# secret_string = {
#                     "engine": "mysql",
#                     "username": "testuser",
#                     "password": "EXAMPLE-PASSWORD",
#                     "host": "my-database-endpoint.us-west-2.rds.amazonaws.com",
#                     "dbname": "myDatabase",
#                     "port": "3306"
#                 }

# #create secret for custom user
# response = client.create_secret(Name='DBProdSecrets2',SecretString='{"username":{custom_user_name}}')

# print(response)
# #

# # retrieve the secret value
# response = client.get_secret_value(SecretId='rds!cluster-ea6cf62c-e20c-4d81-80f7-8e645696e31e')
# secret = ''

# # if the secret is a string, return it directly
# if 'SecretString' in response:
#     print(response['SecretString'])
#     secret = json.loads(response['SecretString'])
#     # # #Connect to mysql rds instance
#     db = pymysql.connect(host='database-1.cluster-chobkoc200g5.us-east-1.rds.amazonaws.com', user = secret['username'], password=secret['password'])

#     # Get list of users
#     cursor = db.cursor()

#     ## executing the statement using 'execute()' method
#     cursor.execute("SELECT user from mysql.user;")

#     ## 'fetchall()' method fetches all the rows from the last executed statement
#     users = cursor.fetchall() ## it returns a list of all databases present

#     ## printing the list of databases
#     print(users)

#     # Create a new user
#     # new_user = 'testuser123'
#     # new_user_password = 'password123'
#     # cursor = db.cursor()
#     # cursor.execute(f"CREATE USER '{new_user}'@'%' IDENTIFIED BY '{new_user_password}'")

#     # # Grant privileges to the user
#     # cursor.execute(f"GRANT SELECT, INSERT, UPDATE ON mydatabase.* TO '{new_user}'@'%'")

#     # # Commit changes and close the connection
#     # db.commit()
#     # cursor.close()
#     # db.close()
#     # print("User created successfully")
# # if the secret is binary, decode it using base64
# else:
#     binary_secret_data = response['SecretBinary']
#     decoded_secret = base64.b64decode(binary_secret_data)
#     print(decoded_secret)

