import requests
import json

query_params = {'access_token': 'API_KEY',
                'link': 'http://bit.ly/YLRxli'}

endpoint = 'https://api-ssl.bitly.com/v3/link/category'
response = requests.get(endpoint, params= query_params)

data = json.loads(response.content)
print data
