import requests

params = {
  'access_key': '8215a42f0f239a637181d7eb2dc4dc74',
  'query': 'india'
}

api_result = requests.get('http://api.weatherstack.com/current', params)
api_response = api_result.json()
print(api_response)
print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))