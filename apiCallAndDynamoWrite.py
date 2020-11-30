import json
import requests
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('pets')

response = requests.get("https://bzy4xhbr70.execute-api.us-east-2.amazonaws.com/test/pets/")

#convert to json
parsed = response.json()
array = []



print(parsed)
print(response)

for item in parsed:
    array_items = {"id":None, "type":None, "price":None}
    array_items['id'] = item['id']
    array_items['type'] = item['type']
    array_items['price'] = item['price']

    array.append(array_items)

    table.put_item(
       Item={
        'id': str(array_items['id']),
        'type': array_items['type'],
        'price': Decimal(str(array_items['price']))
    })

print(array)

# for i in parsed:
    #id = int(parsed['id'])
    #type = parsed['type']
    #price = parsed['price']
    #print("Item Number: ", parsed[i])
    #table.put_item(Item=parsed)