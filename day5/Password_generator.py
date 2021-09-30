#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
count_letters= int(input("How many letters would you like in your password?\n")) 
count_symbols = int(input(f"How many symbols would you like?\n"))
count_numbers = int(input(f"How many numbers would you like?\n"))


password1 = random.sample(letters,count_letters)
password2 = random.sample(symbols,count_symbols)
password3 = random.sample(numbers,count_numbers)
final_password = ''.join(password1)+''.join(password2)+''.join(password3)
#normal printing
print("Normal password:",final_password)
#randamized printingS
print("randomized password:",''.join(random.sample(final_password,len(final_password))))
