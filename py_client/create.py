import requests

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.post(endpoint, json={'title': 'Title 5',
                                             'content': 'Title 5 content',
                                             'price': 69.6})

print(get_response.json())