def lambda_handler(event, context):
    import boto3

    client = boto3.resource('dynamodb', region_name='us-east-1')
    table = client.Table('wolf_db')

    result = table.scan()
    return(result)
