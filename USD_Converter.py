# Python script to be used in Lambda Function
import json
import urllib.request

def convert_usd_to_other_currencies():
    url = "https://api.frankfurter.dev/v1/latest?base=USD"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Request failed: {e}")
        return None

def lambda_handler(event, context):
    print("Converting 1 USD to other currencies")

    # Get conversion rates
    conversion_data = convert_usd_to_other_currencies()

    if conversion_data is None:
        return {
            'statusCode': 500,
            'body': json.dumps('Error fetching conversion rate.')
        }

    # Return the fetched data as the response
    return {
        'statusCode': 200,
        'body': json.dumps(conversion_data)
    }
