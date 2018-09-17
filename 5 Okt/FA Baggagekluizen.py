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
    lijst = file.replace('\n',';')
    lijst = lijst.split(';')
    for x in lijst:
        if x in kluis_lijst:
            kluis_lijst[kluis_lijst.index(x)] = 0
    for x in kluis_lijst:
        if x != 0:
            while True:
                kluis_assign = int(x)
                code = input('Welke code wil je voor je kluis?\n')
                if len(code) <= 3:
                    print('Deze code is niet lang genoeg.')
                elif len(code) >= 4:
                    print('De code is opgeslagen, je hebt kluis '+str(kluis_assign)+' gekregen.\n')
                    open('Files/Kluizen.txt','a').write(str(kluis_assign)+';'+code+'\n')
                    open('Files/Kluizen.txt').close()
                    break
            break

def kluis_openen():
    correct = 0
    for x in range(1,4):
        kluisnummer = input('Wat is je kluisnummer?\n')
        kluis_code = input('Wat is de code van je kluis?\n')
        file = open('Files/Kluizen.txt','r').read()
        if (str(kluisnummer)+';'+str(kluis_code)) in file:
            print('Correct.')
            break
        else:
            print('Incorrect, je hebt nog '+str(3-x)+' pogingen.\n')

def kluis_verwijderen():
    lijst = open('Files/Kluizen.txt', 'r').read()
    open('Files/Kluizen.txt').close()
    lijst = lijst.split('\n')
    for y in range(1,4):
        correct = False
        kluisnr = input('Wat is je kluisnummer?\n')
        kluiscode = input('Wat is je code?\n')
        for x in lijst:
            if (str(kluisnr)+';'+str(kluiscode)) == x:
                lijst[lijst.index(x)] = ''
                correct = True
        if correct == True:
            print('Uw kluis zal uit de lijst worden gehaald.')
            file = ''
            for x in lijst:
                if (x != ''):
                    lijst[lijst.index(x)] = (x+'\n')
            for x in lijst:
                if (x != ''):
                    file = file + x
            open('Files/Kluizen.txt','w').write(file)
            open('Files/Kluizen.txt').close()
            break
        else:
            print('Die combinatie van kluisnummer en kluiscode is niet gevonden.\nJe hebt nog '+str(3-int(y))+' pogingen.')

while True:                                                 #Mainloop
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
        kluis_openen()
    elif menu == 4:
        kluis_verwijderen()
    elif menu == 5:
        break