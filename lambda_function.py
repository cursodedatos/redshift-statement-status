import boto3
import csv

def lambda_handler(event, context):

    statement_id = 'xxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx'
    client = boto3.client('redshift-data')
    response = client.describe_statement(Id=statement_id)
    
    print("Estado:", response['Status'])
    print("SQL:", response['QueryString'])
    if 'Error' in response:
        print("Error:", response['Error'])

    
    return str(response['Status'])
