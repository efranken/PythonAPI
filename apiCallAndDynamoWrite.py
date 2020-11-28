import json
import requests
import boto3

dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('pets')

response = requests.get("https://bzy4xhbr70.execute-api.us-east-2.amazonaws.com/test/pets/")

#convert to json
parsed = response.json()

print(parsed)

for id in parsed:
    id = int(parsed['id'])
    type = parsed['type']
    price = parsed['price']
    print("Adding ID:", id, type)
    table.put_item(Item=parsed)