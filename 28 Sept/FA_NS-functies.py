def standaardprijs(afstandkm: float):
    if (afstandkm <= 50) and (afstandkm > 0):
        prijs = float(afstandkm*0.8)
    elif (afstandkm <= 0):
        prijs = 0
    else:
        prijs = float(15.0+(0.6*afstandkm))
    return prijs

def ritprijs(leeftijd: int, weekendrit: bool, afstandkm: float):
    prijs = standaardprijs(afstandkm)
    if (leeftijd >= 12) and (leeftijd < 65) and (weekendrit == True):
        prijs = prijs * 0.6
    elif ((leeftijd < 12) or (leeftijd >= 65)) and (weekendrit == True):
        prijs = prijs * 0.65
    elif ((leeftijd < 12) or (leeftijd >= 65)) and (weekendrit == False):
        prijs = prijs * 0.7
    return prijs

print(ritprijs(11,False,-20))
print(ritprijs(11,False,20))
print(ritprijs(11,False,70))
print(ritprijs(11,True,-20))
print(ritprijs(11,True,20))
print(ritprijs(11,True,70))
print(ritprijs(12,False,-20))
print(ritprijs(12,False,20))
print(ritprijs(12,False,70))
print(ritprijs(12,True,-20))
print(ritprijs(12,True,20))
print(ritprijs(12,True,70))
print(ritprijs(64,False,-20))
print(ritprijs(64,False,20))
print(ritprijs(64,False,70))
print(ritprijs(64,True,-20))
print(ritprijs(64,True,20))
print(ritprijs(64,True,70))
print(ritprijs(65,False,-20))
print(ritprijs(65,False,20))
print(ritprijs(65,False,70))
print(ritprijs(65,True,-20))
print(ritprijs(65,True,20))
print(ritprijs(65,True,70))