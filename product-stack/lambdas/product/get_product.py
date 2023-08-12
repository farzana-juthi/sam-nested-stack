import json

def lambda_handler(event, context):

    try:
        print("I am in get product page")
        default_headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        }

        return {
            "statusCode": 200,
            "headers": default_headers,
            "body": json.dumps("I am in product get page"),
        }
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)

