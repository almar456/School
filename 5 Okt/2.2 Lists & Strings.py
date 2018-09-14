lijst = eval(input('Geef een lijst met minimaal 10 strings:\n'))
_4lijst = []
for x in lijst:
    if len(x) == 4:
        _4lijst.append(x)
print('De nieuw gemaakte lijst met alle vier-letter strings is:')
print(_4lijst)