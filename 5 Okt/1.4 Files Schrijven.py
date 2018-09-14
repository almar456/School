import datetime
vandaag = datetime.datetime.today()
writefile = open('Files/hardlopers.txt','a')
for x in ['Miranda','Piet','Sacha','Karel','Kemal']:
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, " +x+'\n')
    writefile.write(s)
    print(s)
writefile.close()