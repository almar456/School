def code(invoerstring: str):
    lijst = list(invoerstring)
    string = ''
    for x in lijst:
        lijst[lijst.index(x)] = 3+ord(x)
    for x in lijst:
        lijst[lijst.index(x)] = chr(x)
    for x in lijst:
        string += x
    return string

def ns():
    naam = input('Wat is uw naam?\n')
    start = input('Wat is uw beginstation?\n')
    eind = input('Wat is uw eindstation?\n')
    invoerstring = naam+start+eind
    string = code(invoerstring)
    print('Uw code is: '+string)

ns()