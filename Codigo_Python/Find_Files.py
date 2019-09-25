import boto3
bucket = 'emr-directory'
#Make sure you provide / in the end
prefix = 'JOBS/pasta/'  

client = boto3.client('s3')
result = client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
for o in result.get('CommonPrefixes'):
    print(o.get('Prefix'))
