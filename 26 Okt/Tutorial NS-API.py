def ns(station: str):
    import requests
    import xmltodict

    auth_details = ('almar456@hotmail.com', 'cFATiOO4WL5AXOlOrQgFbTnG5MnLIMZNflOl55ep2qiAHF3kBuuEFw')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+station
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']

            spoornummer = vertrek['VertrekSpoor']['#text']
            typetrein = vertrek['TreinSoort']
            vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]          # 18:36
            print('Om '+vertrektijd+' vertrekt een '+typetrein+' naar '+eindbestemming+' vanaf spoor '+spoornummer+'.')
ns('ut')