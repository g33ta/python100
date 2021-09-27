import random
lst = input('Enter five names:')
splited_lst = lst.split(', ')
random_element = random.randint(0,(len(splited_lst)-1))
print(f"{splited_lst[random_element]} is going to buy the meal today!")


"""2.Instructions
You are going to write a program which will select a random name from a list. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
Line 8 splits the string names_string into individual names and 
puts them inside a List called names. For this to work, you must enter all 
the names as name followed by comma then space. e.g. name, name, name

Example Input\
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!"""