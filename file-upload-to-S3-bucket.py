import boto3

def upload_to_s3(bucket, file_path, object_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket, object_name)
    print(f"Uploaded {file_path} to {bucket}/{object_name}")

# Usage
upload_to_s3("my-devops-bucket", "config.yaml", "configs/config.yaml")
