import boto3

import pprint

from botocore.exceptions import ClientError
# create session with default profile
session = boto3.Session()
ec2_client = boto3.client('ec2')
#Get the list of all regions
region_list = session.get_available_regions('ec2')

regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

#print (regions)

for region in regions:
    ec2_client = boto3.client('ec2', region_name=region)
    #print(f"instance present in {region}")
    response = ec2_client.describe_instances(
        Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
    ],
    DryRun = False
    )

    #print(response)
    for value in response['Reservations']:
        for instance in value['Instances']:
            print(instance['InstanceId'])
            instance_id = instance['InstanceId']
            ec2_client.start_instances(InstanceIds=[instance_id])
            print(f"Instance {instance_id} starting...")
            waiter = ec2_client.get_waiter('instance_running')
            waiter.wait(InstanceIds=[instance_id])
            print(f"Instance {instance_id} start successfully")
    

'''
    try:
        response = ec2_client.describe_instances()
        for instance in response['Reservations']:
            for value in instance['Instances']:
                print(f"instance present in \'{region}\' InstanceId: {value['InstanceId']} and instance state: {value['State']['Name']}")
    except ClientError as e:
        print(f"Error: {e.message}") '''


