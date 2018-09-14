readfile = open('Files/kaartnummers.txt','r')
inhoud = str(readfile.read())
readfile.close()
print('Deze file telt '+str(inhoud.count(','))+' regels.')
inhoud = inhoud.split('\n')
lijst = []
for x in inhoud:
    lijst.append(int((x[0:5])))
print('Het grootste kaartnummer is: '+str(max(lijst))+' dat staat op regel '+str(lijst.index(max(lijst))+1)+'.')