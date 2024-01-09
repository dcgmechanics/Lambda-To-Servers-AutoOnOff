import boto3
region = 'us-east-2'
ec2_instances = ['i-0XXXXXXXXXXXXXXf','i-0XXXXXXXXXXXXXX9']
rds_instance = 'rds-name'
ec2 = boto3.client('ec2', region_name=region)
rds = boto3.client('rds', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=ec2_instances)
    rds.stop_db_instance(DBInstanceIdentifier=rds_instance)
    print('Servers Stopped: ' + str(ec2_instances) + str(rds_instance))