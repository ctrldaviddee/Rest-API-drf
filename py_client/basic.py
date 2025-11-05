import requests

#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

#response = requests.get(url=endpoint,
#                        params={"Hello": "World"},
#                        data={"key": "value"},
#                        json={"key1": "value1"},)

response = requests.post(endpoint, json={'title': 'hey api title', 'content': 'hey api content'})

print(response.json())


