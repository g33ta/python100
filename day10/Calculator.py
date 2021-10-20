from art import logo

def adding(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

def calculator(): 
    print(logo) 
    num1 = int(input("Enter a first number:"))
    operations = {
        '+':adding,
        '-':subtraction,
        '*':multiplication,
        '/':division,
    }
    for operation in operations:
        print(operation)
    while True:
        symble = input("Enter any above symble:")
        num2 = int(input("Enter a next number:"))
        calculation = operations[symble]
        answer = calculation(num1,num2)
        print(f"{num1}{symble}{num2} = {answer}")
        next_calc = input(f"Type y to continue calculation with {answer} or type n to start new calculation: ")
        if next_calc == 'y'.lower():
            num1 = answer
            continue
        else:
            next_calc == 'n'.lower(
            break
    calculator()
        
print(calculator())
