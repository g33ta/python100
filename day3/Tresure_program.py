print('Welcome to Treasure Island')
print('Your mission is to find the treasure.\n')

turn1 = input('Enter Right or Left?').lower()
if turn1 == 'left':
    turn2 = input('Enter Swim or Wait?').lower()
    if turn2 == 'wait':
        door = input('enter which door? Red? Yellow? Blue?').lower()
        if door  == 'yellow':
            print('You win')
        elif door == 'red':
            print('Burned by fire,Game over')
        elif door == 'blue':
            print('Eaten by Beast,Game over')
        else:
            print('Game over')
    else:
        print('Attacked by trout \nGame over')
else:
    print('Fall in to a hole \n Game over')

"""Did with flow chart which is available on gitbooks"""
