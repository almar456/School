def convert(celcius: float):
    fahrenheit = (celcius*1.8)+32
    return fahrenheit
def table():
    print(' F       C')
    for x in [-30,-20,-10,0,10,20,30,40]:
        y = convert(x)
        print('{:5}{:5}'.format(y,x))
table()