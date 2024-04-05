import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
 # Get only running instances
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

print (instances)
for instance in instances:
    print(instance.id)