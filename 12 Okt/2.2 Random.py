import random
def monopolyworp():
    throws = 0
    while throws < 3:
        throw1 = random.randint(1,6)
        throw2 = random.randint(1,6)
        if (throw1 == throw2) and (throws == 2):
            print(str(throw1) + ' + ' + str(throw2) + ' = ' + str(throw2 + throw1) + ' (naar de gevangenis)')
            break
        elif throw2 == throw1:
            print(str(throw1)+' + '+str(throw2)+' = '+str(throw2+throw1)+' (dubbel)')
            throws += 1
        elif throw1 != throw2:
            print(str(throw1) + ' + ' + str(throw2) + ' = ' + str(throw2 + throw1))
            break

monopolyworp()