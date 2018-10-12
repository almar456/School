file = open('Files/producten.csv', 'r').read()
lijst = file.split('\n')
for x in lijst:
    lijst[lijst.index(x)] = x.split(';')
lijst.remove(lijst[0])
lijst.remove(lijst[-1])
prijs = 0
voorraad = 9999999999999
aantal = 0
for x in lijst:
    prijs = max(prijs,float(x[-1]))
    voorraad = min(voorraad,int(x[-2]))
    aantal += float(x[-2])
for x in lijst:
    if str(prijs) in x:
        naam = x[2]
    if str(voorraad) in x:
        artnr = x[0]
print('Het duurste artikel is '+naam+' en die kost '+str(prijs)+' Euro.')
print('Er zijn slechts '+str(voorraad)+' exemplaren in voorraad van het product met nummer '+str(artnr))
print('In totaal hebben wij '+str(aantal)+' producten in voorraad.')