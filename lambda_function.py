
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello this is from AWS SAM Lambda based Application !! Demo Test by Rambabu Vasupilli on 25th Feb 2020. second time')
    }
