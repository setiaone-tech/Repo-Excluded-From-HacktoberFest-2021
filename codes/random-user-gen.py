import requests
url = 'https://randomuser.me/api/1.2/' # Add ?nat=NZ Or Any [Supported] Country Code For Specific Country 
details = requests.get(url)
api = details.json()
print(api)
