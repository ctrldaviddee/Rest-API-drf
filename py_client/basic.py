import requests

#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

#response = requests.get(url=endpoint,
#                        params={"Hello": "World"},
#                        data={"key": "value"},
#                        json={"key1": "value1"},)

response = requests.get(endpoint)

print(response.json()['message'])
print(response.status_code)

