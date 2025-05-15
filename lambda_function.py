import boto3
import csv

def lambda_handler(event, context):

    statement_id = '53271789-cc9f-43df-a344-99329334fe20'
    client = boto3.client('redshift-data')
    response = client.describe_statement(Id=statement_id)
    
    print("Estado:", response['Status'])
    print("SQL:", response['QueryString'])
    if 'Error' in response:
        print("Error:", response['Error'])

    
    return "Salida"
