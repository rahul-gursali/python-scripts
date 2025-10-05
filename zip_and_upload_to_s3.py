import boto3, zipfile

with zipfile.ZipFile("backup.zip", "w") as zipf:
    zipf.write("data.sql")

s3 = boto3.client("s3")
s3.upload_file("backup.zip", "mybucket", "backup.zip")

