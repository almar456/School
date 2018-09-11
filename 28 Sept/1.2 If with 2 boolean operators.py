leeftijd = int(input('Wat is je leeftijd?'+'\n'))
paspoort = input("Heb je een paspoort?"+'\n')
if leeftijd >= 18 and ('ja' in paspoort):
    print('Gefeliciteerd! Je mag stemmen.')
else:
    print('Helaas... Je mag niet stemmen.')
