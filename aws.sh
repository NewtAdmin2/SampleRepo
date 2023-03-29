payload='{"key1": "value1", "key2": "value2", "key3": "value3"}'
output=$(aws lambda invoke --function-name 'testfunction' --payload '{"key1": "value1", "key2": "value2", "key3": "value3"}'  output.json --cli-binary-format raw-in-base64-out)
echo "$output"