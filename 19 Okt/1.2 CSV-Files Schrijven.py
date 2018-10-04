import datetime
import csv

bestand = 'Files/inloggers.csv'
naam = ''
vandaag = datetime.datetime.today().strftime("%a %d %b %Y at %H:%M:%S")
while naam != 'einde':
    naam = input("Wat is je achternaam?\n")
    if naam == 'einde' or naam == 'Einde':
        break
    voorl = input("Wat zijn je voorletters?\n")
    gbdatum = input("Wat is je geboortedatum?\n")
    email = input("Wat is je e-mail adres?\n")
    with open(bestand, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ';')
        csv_writer.writerow([vandaag,voorl,naam,gbdatum,email])
        csv_file.close()