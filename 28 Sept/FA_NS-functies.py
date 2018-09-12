def standaardprijs(afstandkm: float):
    if (afstandkm <= 50) and (afstandkm > 0):
        prijs = float(afstandkm*0.8)
    elif (afstandkm <= 0):
        prijs = 0
    else
        prijs = float(15.0+(0.6*afstandkm))
    return prijs
