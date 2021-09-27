import random
lst = input('Enter five names:')
random_element = random.ranint(0,(len(lst)-1))
print(f"{lst[random_element]} is going to buy the meal today!")