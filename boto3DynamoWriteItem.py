import boto3

dynamodb = boto3.resource('dynamodb')

table=dynamodb.Table('pets')

#do before running put_items to see the count, do again after to verify writing worked
print(table.item_count)

table.put_item(
   Item={
        'id': 'frankie',
        'type': 'cat',
        'price': 'free',
        'age': 4,
    }
)

table.put_item(
   Item={
        'id': 'annabelle',
        'type': 'dog',
        'price': 'free',
        'age': 7,
    }
)

table.put_item(
   Item={
        'id': 'chloe',
        'type': 'cat',
        'price': 'free',
        'age': 10,
    }
)


print(table.item_count)