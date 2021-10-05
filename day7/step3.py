#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the chosen_word is {chosen_word}.')


empty_list = []
for letter in chosen_word:
    empty_list.append('_')
#print(empty_list)

"""TODO-1: - Use a while loop to let the user guess again. 
The loop should only stop once the user has guessed all the letters 
in the chosen_word and 'display' has no more blanks ("_"). 
Then you can tell the user they've won."""
end_of_game = True
while end_of_game :
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess: 
            empty_list[index] = guess
        else:
            pass
        
        if '_' not in empty_list:
            end_of_game = False

    print(empty_list)
    
print('You Won')
