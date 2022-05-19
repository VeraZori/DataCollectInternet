import requests
import json
from pprint import pprint

url = 'https://api.github.com'
user = 'VeraZori'
resp = requests.get(f'{url}/users/{user}/repos')
j_data=resp.json()
#print(j_data['name'])
with open('data.json', 'w') as f:
   json.dump(resp.json(), f)

for i in j_data:
    print(i['name'])
