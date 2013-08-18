import requests
import pprint
query_params = {'apikey': 'a307ebbdfdca47078a370bb69bbc3dad',
                'per_page': 2,
                'page': 5,
                'state': 'NY',
                'start_date': '2012-06-01',
                'end_date': '2012-08-31',
}

endpoint = "http://capitolwords.org/api/text.json"
response = requests.get(endpoint, params=query_params)
data = response.json
pprint.pprint(data)

#request 2 objects per page, and get the 5th page.
#limit the requests to speech from legislators in NY between the first day of 06/12 to the last day of 08/12
