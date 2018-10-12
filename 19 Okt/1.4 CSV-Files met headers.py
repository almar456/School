import csv

with open('Files/producten.csv','a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';' )
    csv_writer.writerow(['Artikelnummer','Artikelcode','Naam','Voorraad','Prijs'])
    csv_writer.writerow([121, 'ABC123', 'Highlight pen', 231, 0.56])
    csv_writer.writerow([123, 'PQR678', 'Nietmachine', 587, 9.99])
    csv_writer.writerow([128, 'ZYX163', 'Bureaulamp', 34, 19.95])
    csv_writer.writerow([137, 'MLK709', 'Monitorstandaard', 66, 32.50])
    csv_writer.writerow([271, 'TRS665', 'Ipad hoes', 155, 19.01])