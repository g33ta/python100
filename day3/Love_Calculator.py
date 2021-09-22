name1 = input('Enter first name:')
name2 = input('Enter Second name:')
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
two_names = lower_case_name1+lower_case_name2 
count1 = 0
for letter in 'true':
    letter1count = two_names.count(letter)
    print(f'{letter} occures {letter1count} times' )
    count1 +=letter1count
    
print('Total = ',count1)
count2 = 0
for letter in 'love':
    letter2count = two_names.count(letter)
    print(f'{letter} occures {letter2count} times' )
    count2 += letter2count
print("Total = ",count2)
add_as_string = str(count1)+str(count2)
score = int(add_as_string)
print(f'Love score is {score} .')

if score<10 or score>90:
    print(f"Your score is {score} , you go together like coke and mentos.")
elif  40<score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




"""Love Calculator
💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together."""


