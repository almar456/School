bestand = 'Files/Gamers.csv'
read = open(bestand, 'r').read()
list = read.split('\n')
for x in list:
    list[list.index(x)] = x.split(';')

Max = 0
for x in list:
    for y in x:
        try:
            value = int(y)
            Max = max(Max,value)
        except:
            pass
for x in list:
    if str(Max) in x:
        print('De hoogste score is: '+x[2]+ ' op '+x[1]+' behaald door '+ x[0]+'.')