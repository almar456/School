invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = invoer.split('-')
intlijst = []
for x in lijst:
    intlijst.append(int(x))
print('Gesorteerde lijst van ints: '+str(sorted(intlijst)))
print('Grootste getal: '+str(max(intlijst))+' en Kleinste getal: '+str(min(intlijst)))
print('Aantal getallen: '+str(len(intlijst))+' en Som van de getallen: '+str(sum(intlijst)))
print('Gemiddelde: '+str(sum(intlijst) / len(intlijst)))