# import boto3
# s3_client = boto3.client('s3',
#                          aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
#                          aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
# response = s3_client.create_bucket(Bucket= 'aqsw654',
#                                    CreateBucketConfiguration= {'LocationConstraint':'ap-south-1'})
# print(response)


import boto3
import pandas as pd
import os

# Define the bucket name and region
bucket_name = 'aqsw654'
region = 'ap-south-1'  # Ensure this matches your AWS configuration

# Create a CSV file to upload
csv_data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}
csv_file = 'sample.csv'
df = pd.DataFrame(csv_data)
df.to_csv(csv_file, index=False)

# Initialize the S3 client using credentials from the AWS configuration file
try:
    s3_client = boto3.client('s3', region_name=region)

    # Create the S3 bucket
    if region == 'us-east-1':
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print(f'Bucket {bucket_name} created successfully')
except Exception as e:
    print(f'Error creating bucket: {e}')

# Upload the CSV file to the S3 bucket
try:
    s3_client.upload_file(csv_file, bucket_name, csv_file)
    print(f'File {csv_file} uploaded successfully to bucket {bucket_name}')
except Exception as e:
    print(f'Error uploading file: {e}')

# Clean up by removing the local CSV file
#os.remove(csv_file)


# import boto3
# mysession=boto3.Session(region_name='ap-south-1')
# s3client=mysession.client("s3")
# bucket_name="aq-15-sriram"
# s3client.create_bucket(Bucket=bucket_name)




