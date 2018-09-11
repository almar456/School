score = int(input('Wat is je score?'+'\n'))
strScore = str(score)
if score >= 15:
    print('Gefeliciteerd!'+'\n')
    print('Met een score van '+strScore+' ben je geslaagd!')
elif score < 15:
    print('Helaas...'+'\n')
    print('Met een score van '+strScore+' ben je gezakt.')
