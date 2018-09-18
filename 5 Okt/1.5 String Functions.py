def removeLeestekens(woordenlijst: list):
    index = -1
    mutable = []
    for x in woordenlijst:
        index = index + 1
        if ('.' in x) or (',' in x) or ('!' in x) or ('?' in x):
            mutable = list(x)
            newword = str('')
            lcount = -1
            if '.' in mutable:
                mutable[mutable.index('.')] = ''
                for x in mutable:
                    lcount = lcount + 1
                    newword = newword + x
                woordenlijst[index] = newword
            elif ',' in mutable:
                mutable[mutable.index(',')] = ''
                for x in mutable:
                    lcount = lcount + 1
                    newword = newword + x
                woordenlijst[index] = newword
            elif '!' in mutable:
                mutable[mutable.index('!')] = ''
                for x in mutable:
                    lcount = lcount + 1
                    newword = newword + x
                woordenlijst[index] = newword
            elif '?' in mutable:
                mutable[mutable.index('?')] = ''
                for x in mutable:
                    lcount = lcount + 1
                    newword = newword + x
                woordenlijst[index] = newword

def gemiddelde():
    string = input('Voer hier een willekeurige zin in:\n')
    woordenlijst = string.split(' ')
    removeLeestekens(woordenlijst)
    wcount = len(woordenlijst)
    gemLengte = 0
    for x in woordenlijst:
        gemLengte = gemLengte + len(x)
    gemLengte = (gemLengte/wcount)
    print(gemLengte)

gemiddelde()