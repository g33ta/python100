#Write your code below this line 👇
def prime_checker(number):
    count = 0
    for num in range(2,number+1):
        if number%num == 0:
            count += 1
            if count>2:
                return str(number) + ' is not prime number'
    else:
        return str(number) + ' is prime number'

            
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
print(prime_checker(number=n))
