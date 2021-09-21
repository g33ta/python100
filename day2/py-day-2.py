#If the bill was $150.00, split between 5 people, with 12% tip. 
#Format the result to 2 decimal places = 33.60
print('Welcome to the tip calculator.')
Total_bill = float(input("What was the total bill?"))
Tip = int(input("What percentage tip would you like to do? 10 ,12 or 15?"))
people_count = int(input('How many people to split the bill?'))
Total_paid =Total_bill+(Total_bill*Tip/100)#dinner +Tip
print(Total_paid)

Each_paid = Total_paid/people_count
print('each person should pay:',round(Each_paid,2))
#Changed
