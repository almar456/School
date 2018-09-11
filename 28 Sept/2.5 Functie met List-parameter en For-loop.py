def kwadraten_som(grondgetallen: list):
    y = int(0)
    for x in grondgetallen:
        if x >= 0:
            y = y + (x**2)
    return y
lijst = [4,5,3,-81]
print(kwadraten_som(lijst))
