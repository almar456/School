string = input('Voer hier een willekeurige zin in:\n')
string = string.replace(',','')
string = string.replace('.','')
woordenlijst = string.split(' ')
wcount = len(woordenlijst)
gemLengte = 0
for x in woordenlijst:
    gemLengte = gemLengte + len(x)
gemLengte = (gemLengte/wcount)
print(gemLengte)