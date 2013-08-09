import requests
import json

query_params = {'access_token': 'API_KEY', 
                'longUrl': 'http://reddit.com/'}

#long Url must be full url

endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = requests.get(endpoint, params=query_params)

data = json.loads(response.content)
print data
