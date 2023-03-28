import boto3

# create a Secrets Manager client
client = boto3.client('secretsmanager',region_name='us-east-1')

# retrieve the secret value
response = client.get_secret_value(SecretId='rds!cluster-ea6cf62c-e20c-4d81-80f7-8e645696e31e')
secret = ''

# if the secret is a string, return it directly
if 'SecretString' in response:
    print(response['SecretString'])
# if the secret is binary, decode it using base64
else:
    binary_secret_data = response['SecretBinary']
    decoded_secret = base64.b64decode(binary_secret_data)
    print(decoded_secret)


# # #Connect to mysql rds instance
# db = pymysql.connect(host=secret['host'], user = secret['username'], password=secret['password'])

# # Create a new user
# new_user = 'testuser123'
# new_user_password = 'password123'
# cursor = db.cursor()
# cursor.execute(f"CREATE USER '{new_user}'@'%' IDENTIFIED BY '{new_user_password}'")

# # Grant privileges to the user
# cursor.execute(f"GRANT SELECT, INSERT, UPDATE ON mydatabase.* TO '{new_user}'@'%'")

# # Commit changes and close the connection
# db.commit()
# cursor.close()
# db.close()
# print("User created successfully")