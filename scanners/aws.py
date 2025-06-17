import boto3

def scan_idle_resources():
    ec2 = boto3.client('ec2')
    idle_resources = []
    
    # Find stopped instances
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    for r in instances['Reservations']:
        for i in r['Instances']:
            idle_resources.append({'type': 'EC2', 'id': i['InstanceId'], 'state': i['State']['Name']})

    # Unattached EBS
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    for v in volumes['Volumes']:
        idle_resources.append({'type': 'EBS', 'id': v['VolumeId']})

    return idle_resources
