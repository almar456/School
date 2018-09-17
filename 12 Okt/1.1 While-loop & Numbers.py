som = []
getal = 1
while getal != 0:
    getal = int(input('Geef een getal: '))
    som.append(getal)
print('Er zijn '+str(len(som)-1)+' getallen ingevoerd, de som is '+str(sum(som))+'.')