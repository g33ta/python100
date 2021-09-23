print('Welcome to Treasure Island')
print('Your mission is to find the treasure.\n')

t1 = input('Enter Right or Left?')
turn1 = t1.lower()
if turn1 == 'left':
    t2 = input('Enter Swim or Wait?')
    turn2 = t2.lower()
    if turn2 == 'wait':
        door = input('enter which door? Red? Yellow? Blue?')
        if door  == 'yellow':
            print('You win')
        elif door == 'red':
            print('Burned by fire,Game over')
        elif door == 'blue':
            print('Eaten by Beast,Game over')
        else:
            print('Game over')
    elif turn2 == 'swim':
        print('Attacked by trout \nGame over')
    else:
        print('Attacked by trout \nGame over')

elif turn1 == 'right':
    print('Fall in to a hole \n Game over')
else:
    print('Fall in to a hole \n Game over')
