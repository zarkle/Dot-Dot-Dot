def lambda_handler(event, context):
    import boto3  # wolf_db

    client = boto3.resource('dynamodb', region_name='us-east-1')  # wolf_db
    table = client.Table('wolf_db')  # wolf_db create table instance

    result = table.scan()
    return(result)
