import xmltodict

file = open('Files/Stationslijsten.xml', 'r').read()
file = xmltodict.parse(file)

print('Dit zijn de codes en types van de vier stations:')
for x in file['Stations']['Station']:
    print(x['Code']+' - '+x['Type'])

print('\nDit zijn alle stations met één of meer synoniemen:')
lijst = []
string = ''
for x in file['Stations']['Station']:
    if x['Synoniemen'] != None:
        lijst = lijst + x['Synoniemen']['Synoniem']
        code = x['Code']
for x in range(0,len(lijst)):
    if x != len(lijst)-1:
        string += lijst[x] + ', '
    else:
        string += lijst[x]
print(code+' - '+string)

print('\nDit zijn de codes en lange namen van de vier stations:')
for x in file['Stations']['Station']:
    print(x['Code']+' - '+x['Namen']['Lang'])