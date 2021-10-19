import art
import os

print(art.logo) 

print('Welcome to secret Auction program')
dic_of_bidders = {}
while True:
    Name = input("Enter your name:")
    Bid  = int(input("Enter your bid:"))
    dic_of_bidders[Name] = Bid
    end_of_bidding = input("Are there any bidders:y or n?")
    if end_of_bidding == 'y'.lower():
        os.system('cls')
        continue
    else:
        lst  = []
        for key,value in dic_of_bidders.items():
            lst.append(value)
        break
max_no = 0
for key,value in dic_of_bidders.items():
    if value > max_no:
        max_no = value
    else:
        pass
print(f"the Winner is {key} with a bid of ${max_no}")
    
    # if max(lst) == value:
    #     print(f"the Winner is {key} with a bid of {max(lst)}")
    # else:
    #     pass
    


