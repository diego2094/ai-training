import boto3

s3 = boto3.client('s3')

bucket_name = 'ai-testing-temp'

file_name = 'sample.txt'

s3_key = 'uploads/sample.txt'

try:

    s3.upload_file(file_name, bucket_name, s3_key)

    print(f"File '{file_name}' uploaded successfully to '{bucket_name}/{s3_key}'")

except Exception as e:

    print(f"Error uploading file: {e}")