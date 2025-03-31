import boto3

ec2 = boto3.client('ec2')
instances = ec2.describe_instances()

for res in instances["Reservations"]:
    for inst in res["Instances"]:
        print(inst["InstanceId"], inst["State"]["Name"])
