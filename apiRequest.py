import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://bzy4xhbr70.execute-api.us-east-2.amazonaws.com/test/pets/")

jprint(response.json())