def seizoen(maand: int):
    if ((maand <= 2) and (maand > 0)) or (maand == 12):
        return'Winter'
    elif (maand >= 3) and (maand < 6):
        return'Lente'
    elif (maand >= 6) and (maand < 9):
        return'Zomer'
    elif (maand >= 9) and (maand < 12):
        return'Herfst'
print(seizoen(12))