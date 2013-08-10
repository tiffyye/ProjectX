import requests
import pprint


#Search for the phrase 'holiday season' occurring between November 1, 2012 and December 31, 2012.

query_params = { 'apikey': 'API_KEY',
                 'per_page': 3,
                 'phrase': 'holiday season',
                 'start_date':'2012-11-01',
                 'end_date':'2012-12-31'
}

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get(endpoint, params=query_params)

data = response.json
pprint.pprint(data)

