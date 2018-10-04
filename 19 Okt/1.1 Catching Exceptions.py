try:
    aantal = input('Hoeveel personen gaan er mee op reis?\n')
    aantal = int(aantal)
    if aantal < 0:
        print('Negatieve getallen mogen niet!')
    if aantal >= 0:
        prijs = str(4356/aantal)
        print('De prijs per persoon is '+prijs+' euro.')

except ValueError:
    print('Gebruik cijfers om het aantal in te voeren.')
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except:
    print('Onjuiste invoer!')