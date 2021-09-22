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





