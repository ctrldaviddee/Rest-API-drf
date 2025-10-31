import requests

endpoint = 'https://httpbin.org/anything'

response = requests.get(url=endpoint,
                        params={"Hello": "World"},
                        data={"key": "value"},
                        json={"key1": "value1"},)

print(response.text)
