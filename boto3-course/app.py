import boto3
import os
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

s3=boto3.resource('s3', 
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name='ap-south-1'
)
# list buckets
for bucket in s3.buckets.all():
    print(bucket.name)

#create a bucket
BUCKET_NAME = 'devops-bucket-tutedude'
# s3.create_bucket(
#     Bucket=BUCKET_NAME,
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1'
#     }
# )
# print(f'Bucket {BUCKET_NAME} created')

#delete a bucket
# s3.Bucket(BUCKET_NAME).delete()
# print(f'Bucket {BUCKET_NAME} deleted')

# read a file from the bucket
# s3.Bucket(BUCKET_NAME).download_file('ManufacturingDataset.csv', 'test.txt')

# upload a file to the bucket
# s3.Bucket(BUCKET_NAME).upload_file('test2.txt', 'test2.txt')


# AWS param store
# ssm = boto3.client('ssm', 
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#     region_name='ap-south-1'
# )
# response = ssm.get_parameter(Name='eggs', WithDecryption=True)
# print(response['Parameter']['Value'])