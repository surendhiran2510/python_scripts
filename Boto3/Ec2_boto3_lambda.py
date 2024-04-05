import json

import boto3

def lambda_handler(event, context):
    
    # create a client Object for Ec2 #using the default session
    ec2_client = boto3.client('ec2')
    
    # step:1 Get the list of all regions

    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    print (regions)

    #Step: 2 for each_region get the reponse of describe_instances()
    
    for region in regions:
        ec2_client = boto3.client('ec2', region_name=region)
        #print(region)
        response = ec2_client.describe_instances(
            Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running',
                ]
            },
        ],
        DryRun = False
        )
        
        #print(response)
    #step:3 Parse the Response and get the Instance-id for running instance
        for value in response['Reservations']:
            for instance in value['Instances']:
                print(instance['InstanceId'])
                instance_id = instance['InstanceId']
                
    # step:4 Stop the instance using stop_instances()
                ec2_client.stop_instances(InstanceIds=[instance_id])
                print(f"Instance {instance_id} stopping...")
    # Create waiter Client for instance_stopped and call the wait method with 'instance-id'
    # check the instance state every 15 seconds
                waiter = ec2_client.get_waiter('instance_stopped')
                waiter.wait(InstanceIds=[instance_id])
                print(f"Instance {instance_id} stopped successfully")
                
                