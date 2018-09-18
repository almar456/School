def ticker(filename: str):
    file = open('Files/'+filename,'r').read()
    file = file.split('\n')
    for x in file:
        file[file.index(x)] = x.split(':')
    tickers = {}
    for x in file:
        tickers.update({x[0]:x[1]})
    return tickers

file = ticker('tickers.txt')

c_name = input('Enter company name: ')
if c_name in file:
    print('Ticker Symbol: '+file[c_name])
else:
    print('Invalid company name.')

t_symbol = input('Enter ticker symbol: ')
correct = False
for x in file.items():
    if x[1] == t_symbol:
        print('Company name: '+x[0])
        correct = True
if correct == False:
    print('Invalid ticker symbol.')