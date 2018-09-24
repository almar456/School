def inlezen_beginstation(stations: list):
    while True:
        ms = False
        beginstation = input('Wat is uw beginstation?\n')
        if beginstation == 'Maastricht':
            ms = True
            print('Dat is het eindpunt van de trein.\n')

        elif beginstation != 'Maastricht':
            for x in stations:
                if x == beginstation:
                    print('Uw beginstation is '+beginstation+'.\n')
                    return beginstation
        if ms == False:
            print('Deze trein gaat niet naar dat station.\n')

def inlezen_eindstation(stations: list,beginstation: str):
    while True:
        correct = False
        while True:
            eindstation = input('Wat is uw eindstation?\n')
            for x in stations:
                if x == eindstation:
                    correct = True
                    break
            if correct == True:
                break
            print('Deze trein gaat niet naar dat station.\n')
        if not (stations.index(eindstation) < stations.index(beginstation)):
            print('Uw eindstation is ' + eindstation + '.\n')
            return eindstation
        print('Het eindstation ligt voor het beginstation\n')

def omroepen_reis(stations: list, beginstation: str, eindstation: str):
    afstand = stations.index(eindstation)-stations.index(beginstation)
    print('Het beginstation '+beginstation+' is het '+str(stations.index(beginstation)+1)+'e station in het traject.')
    print('Het eindstation ' + eindstation + ' is het ' + str(
        stations.index(eindstation) + 1) + 'e station in het traject.')
    print('De afstand bedraagt '+str(afstand)+' station(s).')
    print('De prijs van het kaartje is '+str(afstand*5)+' euro.')
    print('\nJij stapt in de trein in: '+beginstation)
    I = stations.index(beginstation)+1
    I_eindstation = stations.index(eindstation)
    while I < I_eindstation:
        print('- '+stations[I])
        I += 1
    print('Jij stapt uit in: '+eindstation)

stations = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal',
            'Amsterdam Amstel','Utrecht Centraal','s-Hertogenbosch','Eindhoven','Weert','Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)