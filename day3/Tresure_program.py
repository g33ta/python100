print('Welcome to Treasure Island')
print('Your mission is to find the treasure.\n')

turn1 = input('Enter Right or Left?').lower()
if turn1 == 'left':
    turn2 = input('Enter Swim or Wait?').lower()
    if turn2 == 'wait':
        door = input('enter which door? Red? Yellow? Blue?').lower()
        if door  == 'yellow':
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
            print('You win')
        elif door == 'red':
            print('''(  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
            print('Burned by fire,Game over')
        elif door == 'blue':
            print('''(    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"''')
            print('Eaten by Beast,Game over')
        else:
            print('Game over')
    else:
        print(''',__
                   |  `'.
__           |`-._/_.:---`-.._
\='.       _/..--'`__         `'-._
 \- '-.--"`      ===        /   o  `',
  )= (                 .--_ |       _.'
 /_=.'-._             {=_-_ |   .--`-.
/_.'    `\`'-._        '-=   \    _.'
    jgs  )  _.-'`'-..       _..-'`
        /_.'        `/";';`|
                     \` .'/
                      '--''')
        print('Attacked by trout \nGame over')
else:
    print('''_           _      
| |         | |     
| |__   ___ | | ___ 
| '_ \ / _ \| |/ _ \
| | | | (_) | |  __/
|_| |_|\___/|_|\___|''')
    print('Fall in to a hole \n Game over')

"""Did with flow chart which is available on gitbooks"""




