import boto3
import csv

def lambda_handler(event, context):
    print (event)
    # Configuración
    REGION = 'us-east-1'
    S3_PATH = 's3://curso-datos-udla-prueba/bank.csv'
    REDSHIFT_WORKGROUP = 'udla-6'
    REDSHIFT_DATABASE = 'dev'
    REDSHIFT_TABLE = 'bank'
    iam_role_arn = 'arn:aws:iam::799412981296:role/service-role/AmazonRedshift-CommandsAccessRole-20250515T173057'

    # Inicializar cliente boto3
    client = boto3.client('redshift-data', region_name=REGION)

    # Comando COPY
    copy_sql = f"""
    COPY {REDSHIFT_TABLE}
    FROM '{S3_PATH}'
    IAM_ROLE '{iam_role_arn}'
    DELIMITER ';'
    IGNOREHEADER 1
    REGION '{REGION}'
    TIMEFORMAT 'auto'
    FORMAT AS CSV;
    """

    #response = client.execute_statement(
    #    WorkgroupName=REDSHIFT_WORKGROUP,
    #    Database=REDSHIFT_DATABASE,
    #    Sql=copy_sql
    #)
    #print("Carga iniciada. Statement ID:", response['Id'])

    #         SecretArn= "arn:aws:secretsmanager:us-east-1:799412981296:secret:cred-redshift-xi6CUL"

    statement_id = '53271789-cc9f-43df-a344-99329334fe20'
    client = boto3.client('redshift-data')
    response = client.describe_statement(Id=statement_id)
    
    print("Estado:", response['Status'])
    print("SQL:", response['QueryString'])
    if 'Error' in response:
        print("Error:", response['Error'])

    
    return "Salida"
