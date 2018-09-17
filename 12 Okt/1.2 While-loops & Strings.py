while True:
    string = input('Geef een string van vier letters: ')
    if len(string) == 4:
        print('Inlezen van correcte string '+string+' is geslaagd.')
        break
    else:
        print(string+' heeft '+str(len(string))+' letters.')