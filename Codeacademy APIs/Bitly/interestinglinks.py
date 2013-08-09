import requests
import json

query_params = {'access_token': 'API_KEY',
                'query': 'pizza', #search word
                'limit':1} #number of results returned, 1 is default, up to 10

endpoint = 'https://api-ssl:bitly.com/v3/search'
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)
print data
