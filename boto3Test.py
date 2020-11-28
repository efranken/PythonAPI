import boto3

dynamodb = boto3.resource('dynamodb')

# code used to create the table 
# table = dynamodb.create_table(
#     TableName='pets',
#     KeySchema=[
#         {
#             'AttributeName': 'id',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'type',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'id',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'type',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# table.meta.client.get_waiter('table_exists').wait(TableName='PETS')

table=dynamodb.Table('pets')

print(table.item_count)