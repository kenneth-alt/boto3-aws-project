import os
import time
import boto3

# Get the AWS credentials and region from environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_REGION')

# Create an EC2 client object with the specified region and credentials
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Get the current region
region = ec2.meta.region_name

# Get a list of all security groups in the region
security_groups = ec2.describe_security_groups()

# Create an array of idle security groups
idle_groups = []

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
        idle_groups.append(sg)

    with open('idle_security_groups.txt', 'w') as f:
        for sg in idle_groups:
            f.write(f"Region: {region}\nName: {sg['GroupName']}\nID: {sg['GroupId']}\nDescription: {sg['Description']}\n\n")
            

# Print a message indicating the number of idle security groups found
print(f"Found {len(idle_groups)} idle security groups in {aws_region}. Check idle_security_groups.txt in home directory for details.")

while True:
    print("Container still running")
    time.sleep(60)
