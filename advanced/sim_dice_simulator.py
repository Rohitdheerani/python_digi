import random

while True:
    input('enter to roll dice๐ฒ') 
    roll = random.randint(1, 6)
    print ('you rolled dice and got ๐ฒ:',roll)
    if roll == 1:
        print('๐you lose!๐')
        break
    elif roll == 6:
        print('๐you win!๐')
        break
    else:
        print('keep rolling...')