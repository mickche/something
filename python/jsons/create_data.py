import requests
import pprint
import json
resp  = requests.get("https://jsonplaceholder.typicode.com/posts")

data = resp.json()

print(data[0])
