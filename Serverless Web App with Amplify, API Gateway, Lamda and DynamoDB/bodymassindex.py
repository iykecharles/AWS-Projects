import json
import boto3
from time import gmtime, strftime


mydynamodb = boto3.resource("dynamodb")
table_name = mydynamodb.Table("bodyMassIndexCalculation")

def lambda_handler(event, context):
    #current_time_millis = str(int(round(time.time() * 1000)))
    bmi = (number1/(number2*number2))
    name = event['name']
    number1 = event['number1']
    number2 = event['number1']

    response = table_name.put_item(
    Item={
        'ID': bmi,
        'name': name,
        'number1': number1,
        'number2': number2
        
    }
        
)


    return {
        'statusCode': 200,
        'body': json.dumps('Hello! your body mass index is ', bmi)
    }
# Function to add a new entry into the DynamoDB table


