import requests
import json


with open('wix_account_id.token') as f:
    account_id=f.read().strip('\n')
with open('wix_api_key.token') as f:
    api_key=f.read().strip('\n')

# Récupération du site_id
url = 'https://www.wixapis.com/site-list/v2/sites/query'

headers = {'Content-Type': 'application/json',
           'Authorization': api_key,
           'wix-account-id': account_id
           }

response = requests.post(url, headers=headers)

site_id = response.json()['sites'][0]['id']

# On ajoute le site_id au Headers de la requete
headers['wix-site-id'] = site_id

url = 'https://www.wixapis.com/stores/v1/products/query'

query = '{"query":{"sort":"[{\\"numericId\\": \\"asc\\"}]"}}'

response = requests.post(url, headers=headers, data=query)
print (response)
json_response = response.json()

with open('products.json', 'w') as f:
    f.write(json.dumps(json_response))