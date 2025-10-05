import os
import shutil
import boto3
from datetime import datetime

S3_BUCKET_NAME = "s3-bucket-name"  
S3_OBJECT_PREFIX = "backups/"           # S3 folder (key prefix)
REGION_NAME = "us-east-1"               

def create_zip_and_upload(bucket_name, s3_prefix=""):
    """
    Creates a ZIP archive of the current working directory and uploads it to S3.
    """
    
    # 1. Define filenames and paths
    current_dir = os.getcwd()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Name for the zip file (excluding the .zip extension for shutil.make_archive)
    archive_base_name = f"current_directory_backup_{timestamp}" 
    
    # This will create a file named 'current_directory_backup_YYYYMMDD-HHMMSS.zip'
    zip_filename = f"{archive_base_name}.zip"
    
    # The full S3 object key (path/filename)
    s3_object_key = os.path.join(s3_prefix, zip_filename)

    print(f"Starting backup of directory: {current_dir}")
    
    try:
        # 2. Create the ZIP Archive using shutil
        # 'base_name': The name of the file to create (without extension)
        # 'format': The archive format (e.g., 'zip', 'tar', 'gztar')
        # 'root_dir': The directory to start archiving from (current directory)
        shutil.make_archive(
            base_name=archive_base_name,
            format='zip',
            root_dir=current_dir
        )
        print(f"Successfully created ZIP file: {zip_filename}")

        # 3. Upload the ZIP file to S3
        s3 = boto3.client('s3', region_name=REGION_NAME)
        
        print(f"Uploading to s3://{bucket_name}/{s3_object_key}...")
        
        s3.upload_file(
            Filename=zip_filename, 
            Bucket=bucket_name, 
            Key=s3_object_key
        )
        
        print("Upload complete!")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # 4. Clean up the local ZIP file
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
            print(f"Cleaned up local file: {zip_filename}")
        else:
            print(f"Could not find local file {zip_filename} to clean up.")

# --- Execute the script ---
if __name__ == "__main__":
    create_zip_and_upload(S3_BUCKET_NAME, S3_OBJECT_PREFIX)
