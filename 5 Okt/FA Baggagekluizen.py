import sys                                                          #Imports


def toon_aantal_kluizen_vrij():                                     #Functiedefinities
    file = open('Files/Kluizen.txt','r').read()
    aantal_bezet = int(file.count(';'))
    aantal_vrij = 12 - aantal_bezet
    open('Files/Kluizen.txt').close()
    return aantal_vrij

def nieuwe_kluis():
    kluis_lijst = ['1','2','3','4','5','6','7','8','9','10','11','12']
    file = open('Files/Kluizen.txt','r').read()
    open('Files/Kluizen.txt').close()
    lijst = file.split(';')
    for x in lijst:
        if x in kluis_lijst:
            kluis_lijst[kluis_lijst.index(x)] = 0
    for x in kluis_lijst:
        if x != 0:
            valid_code = 0
            while valid_code == 0:
                kluis_assign = int(x)
                code = input('Welke code wil je voor je kluis?\n')
                if len(code) <= 3:
                    print('Deze code is niet lang genoeg.')
                elif len(code) >= 4:
                    print('De code is opgeslagen, je hebt kluis '+str(kluis_assign)+' gekregen.\n')
                    open('Files/Kluizen.txt','a').write(str(kluis_assign)+';'+code+'\n')
                    open('Files/Kluizen.txt').close()
                    valid_code = 1

            break



stop = 0
while stop == 0:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn.\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Ik wil stoppen\n')
    menu = input()
    try:
            menu = int(menu)
    except:
        print('Dat is geen correct nummer.')
        sys.exit(0)

    if (menu < 1) or (menu > 5):
        print('Dat is geen correct nummer.')
        sys.exit(0)
    elif menu == 1:
        aantal_vrij = toon_aantal_kluizen_vrij()
        print('Er zijn op dit moment '+str(aantal_vrij)+' kluizen beschikbaar.\n')
    elif menu == 2:
        nieuwe_kluis()
    elif menu == 3:
        print(3)
    elif menu == 4:
        print(4)
    elif menu == 5:
        stop = 1