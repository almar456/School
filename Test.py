import requests

auth_details = ('almar456@hotmail.com', 'cFATiOO4WL5AXOlOrQgFbTnG5MnLIMZNflOl55ep2qiAHF3kBuuEFw')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)
string = response.text
print(string)