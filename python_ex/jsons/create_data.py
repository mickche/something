import requests
import json

def create_data(url:str) -> list[dict]:
    resp  = requests.get(url)
    data = resp.json()
    return data

# print(create_data("https://jsonplaceholder.typicode.com/posts"))


# in dict: userId; id; title; body

