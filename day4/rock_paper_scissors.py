import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
"""code written based on conditions of game and it is located under the program"""
# person = int(input('Enter O or 1 or 2:'))
# print(f"Your choice is {person}:")

# if person == 0 :
#     print(rock)
# elif person == 1 :
#     print(paper)
# elif person == 2:
#     print(scissors)
# else:
#     print("please enter range from 0-2" )

# computer = random.randint(0,2)
# print(f"computer choice is {computer}:")
# if computer == 0:
#     print(rock)
# elif computer == 1:
#     print(paper)
# elif computer == 2:
#     print(scissors)

# if person >=3 or person<0:
#     print('plese enter number from 0-2')
# elif person == 0 and computer == 2 :
#     print("i am the winner")
# elif person == 2 and computer == 1:
#     print('I am the winner')
# elif person == 1 and computer == 0:
#     print("i am the winner")
# elif person == computer:
#     print("game is tie")
# else:
#     print("You lose")

#implemented program
lst = [rock,paper,scissors]
person = int(input('Enter O or 1 or 2:'))
print(f"Your choice is {person}:")
print(lst[person])

computer = random.randint(0,2)
print(f"computer choice is {computer}:")
print(lst[computer])

if person >=3 or person<0:
    print('plese enter number from 0-2')
elif person == 0  and computer == 2 :
    print("i am the winner")
elif person == 2 and computer == 1:
    print('I am the winner')
elif person == 1 and computer == 0:
    print("i am the winner")
elif person == computer:
    print("game is tie")
else:
    print("You lose")


"""What are the rules of RPS?

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock."""