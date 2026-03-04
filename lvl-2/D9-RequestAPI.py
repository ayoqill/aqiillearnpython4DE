# request API

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json() # Convert the response to JSON format

print(data)