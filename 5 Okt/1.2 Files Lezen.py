readfile = open('Files/kaartnummers.txt','r')
inhoud = str(readfile.read())
readfile.close()
inhoud = inhoud.split('\n')
for x in inhoud:
    print(x[8:]+' heeft kaartnummer: '+x[0:5])