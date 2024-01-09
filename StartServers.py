import boto3
region = 'us-east-2'
ec2_instances = ['i-0XXXXXXXXXXXXXXf','i-0XXXXXXXXXXXXXX9']
rds_instance = 'rds-name'
ec2 = boto3.client('ec2', region_name=region)
rds = boto3.client('rds', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=ec2_instances)
    rds.start_db_instance(DBInstanceIdentifier=rds_instance)
    print('Servers Started: ' + str(ec2_instances) + str(rds_instance)