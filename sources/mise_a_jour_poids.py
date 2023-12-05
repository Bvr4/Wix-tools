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

# query = '{"query":{"sort":"[{\\"numericId\\": \\"asc\\"}]"}}'
query = '{"query":{"sort":"[{\\"numericId\\": \\"asc\\"}]","filter":"{\\"numericId\\": {\\"$gt\\": 1669460978142000}}"}}'

response = requests.post(url, headers=headers, data=query)
produits = response.json()

for produit in produits['products']:
    print("///")
    print(produit['id'] + " - " + produit['name'])

    if produit['name'].lower().endswith('coton'):
        if 'choices' in produit['productOptions'][0]:
            id = produit['id']
            url = f'https://www.wixapis.com/stores/v1/products/{id}/variants'

            payload = {"variants":[{"choices": {"Quantité": "Par multiple de 10 cm"}, "weight": 0.021},{"choices": {"Quantité": "Par coupon de 50 cm"}, "weight": 0.105},{"choices": {"Quantité": "Au mètre"}, "weight": 0.210}]}

            response = requests.patch(url, headers=headers, json=payload)
            print(response)
            # json_response = response.json()
            # print(json_response)

    elif produit['name'].lower().endswith('jersey'):
        if 'choices' in produit['productOptions'][0]:
            id = produit['id']
            url = f'https://www.wixapis.com/stores/v1/products/{id}/variants'

            payload = {"variants":[{"choices": {"Quantité": "Par multiple de 10 cm"}, "weight": 0.032},{"choices": {"Quantité": "Par coupon de 50 cm"}, "weight": 0.160},{"choices": {"Quantité": "Au mètre"}, "weight": 0.320}]}

            response = requests.patch(url, headers=headers, json=payload)
            print(response)
            # json_response = response.json()
            # print(json_response)


# id = '550295e1-e917-2280-d111-fd8c04e67ffa'

# url = f'https://www.wixapis.com/stores/v1/products/{id}/variants'

# query = {
#             "variants": [
#                 {
#                     "choices": {
#                         "Quantité": "Par multiple de 10 cm"
#                     },
#                     "weight": 0.021
#                 },
#                 {
#                     "choices": {
#                         "Quantité": "Par coupon de 50 cm"
#                     },
#                     "weight": 0.105
#                 },
#                 {
#                     "choices": {
#                         "Quantité": "Au mètre"
#                     },
#                     "weight": 0.210
#                 }
#             ]
#         }

# response = requests.patch(url, headers=headers, json=query)
# print(response)
# json_response = response.json()
# print(json_response)

#######################################################

# url = f'https://www.wixapis.com/stores-reader/v1/products/{id}/variants/query'

# query = '{"query":{"sort":"[{\\"numericId\\": \\"asc\\"}]"}}'
# # query = '{"query": {\\"variantIds\\": [\\"ae712afd-6574-4725-9991-9700acb7d0ae\\"]}}'

# # query = '{"querry":  {\\"choices\\": {\\"Quantité\\": \\"Par multiple de 10 cm\\"}}}'


# response = requests.post(url, headers=headers)
# print(response)
# json_response = response.json()

# with open('product_variants_1.json', 'w') as f:
#     f.write(json.dumps(json_response))