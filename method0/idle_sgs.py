import os
import boto3

# Get the AWS credentials and region from environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_REGION')

# Create an EC2 client object with the specified region and credentials
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


# Get a list of all security groups in the region
security_groups = ec2.describe_security_groups()

# Loop through each security group and check if it's being used
for sg in security_groups['SecurityGroups']:
    # Get a list of all instances using the security group
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance.group-id',
                'Values': [sg['GroupId']]
            }
        ]
    )

    # If there are no instances using the security group, print the group ID, name, and description
    if not instances['Reservations']:
        print(f"Name: {sg['GroupName']}\nID: {sg['GroupId']}\nDescription: {sg['Description']}\n\n")