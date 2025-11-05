import requests

try:
    product_id = int(input('Enter the product id: '))
except:
    product_id = None
    print(f'{product_id} is not valid input')

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'
    print(requests.delete(endpoint).status_code)