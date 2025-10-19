import boto3

ec2 = boto3.client('ec2')
instance_id = "i-1234567890abcdef"

ec2.stop_instances(InstanceIds=[instance_id])
print("EC2 Instance Stopped")
