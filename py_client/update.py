import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

response = requests.put(endpoint, json={'title' : 'UPdated title', 'price' : 10.})

print(response.json())