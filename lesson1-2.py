import requests
import json
from pprint import pprint
url='https://api.vk.com/method/groups.get?extended=1&v=5.131&access_token=*****0ee5cd045e08f5b503167de2e88fb298127c8980261424a07c81c5b878b723245a5e43'
resp=requests.get(url)
j_data= resp.json()
with open('data2.json', 'w') as f:
   json.dump(resp.json(), f)

for item in j_data['response']['items']:
 print(item['name'])