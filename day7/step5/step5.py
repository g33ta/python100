#Step5
import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game
print(hangman_art.logo)

#Testing code
print(f'Pssst, the chosen_word is {chosen_word}.')

empty_list = []
for letter in chosen_word:
    empty_list.append('_')

lives = 6
game_over = False
while not game_over:
    guess = input('guess a letter:')


#TODO-4: - If the user has entered a letter they've already guessed, 
# print the letter and let them know.
    if  guess in empty_list:
        print(f'You already entered {guess}. Please enter another letter')
        continue
    
    
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                empty_list[position] = guess
        print(empty_list)
        print(hangman_art.stages[lives])
        if  '_' not in  empty_list:
            game_over = True
            print('You won the game')
        else:
            continue
        
        
    else:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter
        #  and let them know it's not in the word.
    
        lives -= 1
        print(f'guessed letter {guess} is not in {chosen_word}')
        print(f'lives count is {lives}')
        print(hangman_art.stages[lives])
        
        if lives == 0:
            game_over = True
            print(f'You lost your lives')
        else:
            continue  
#TODO-2: - Import the stages from hangman_art.py and make this error go away.