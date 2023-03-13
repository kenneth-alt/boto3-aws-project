import os
import boto3

# Get the AWS credentials and region from environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_REGION')

# Create an EC2 client object with the specified region and credentials
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Retrieve all security groups
response = ec2.describe_security_groups()
security_groups = response['SecurityGroups']

# Iterate over the security groups
for sg in security_groups:
    group_id = sg['GroupId']
    
    # Check if any instance is using the security group
    response = ec2.describe_instances(Filters=[{'Name': 'instance.group-id', 'Values': [group_id]}])
    reservations = response['Reservations']
    
    if not reservations:
        #print(f"Security group {group_id} is not used by any instance")
        print(f"Unused Security Group ID: {sg['GroupId']}\nName: {sg['GroupName']}\nDescription: {sg['Description']}\n")