#Step4
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the chosen_word is {chosen_word}.')

empty_list = []
for letter in chosen_word:
    empty_list.append('_')

lives = 6
game_over = False
while not game_over:
    guess = input('guess a letter:')
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                empty_list[position] = guess
        print(empty_list)
        print(stages[lives])
        if  '_' not in  empty_list:
            game_over = True
            print('Game over')
        else:
            continue
        
        
    else:
    
        lives -= 1
        print(f'guess letter {guess} is not in {chosen_word}')
        print(f'lives count is {lives}')
        print(stages[lives])
        
        if lives == 0:
            game_over = True
            print('Game over')
        else:
            continue  


          

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print
    #  "You lose."

    #Join all the elements in the list and turn it into a String.
    #TODO-3: - print the ASCII art from 'stages' that corresponds 
    # to the current number of 'lives' the user has remaining.