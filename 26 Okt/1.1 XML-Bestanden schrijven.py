import xmltodict
myXMLfile = open('Files/Artikelen.xml','r').read()
dictionary = xmltodict.parse(myXMLfile)
for x in dictionary['artikelen']['artikel']:
    print(x['naam'])