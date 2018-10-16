def namen():
    dictionary = {}
    while True:
        naam = input('Volgende naam: ')
        if naam in dictionary:
            dictionary.update({naam:(dictionary[naam]+1)})
        elif naam == '':
            break
        else:
            dictionary.update({naam:1})
    for x in dictionary.items():
        if x[1] == 1:
            print('Er is 1 student met de naam '+x[0]+'.')
        else:
            print('Er zijn '+str(+x[1])+' studenten met de naam '+x[0]+'.')

namen()