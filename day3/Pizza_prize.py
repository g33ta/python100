Small_Pizza  = 15
Medium_Pizza = 20
Large_Pizza = 25
Pepperoni_for_Small_Pizza = 2
Pepperoni_for_Medium_or_Large_Pizza = 3
Extra_cheese_for_any_size_pizza = 1
pizza_size = input('Which size oof pizza you want ?L or M or S?')
Extra_addings = input('Do yo want to add pepperoni? y or n:')
Extra_cheese = input('Do you want  to add Cheese?y or n:')

# if pizza_size == 'S':
#     if Extra_addings == "y" and Extra_cheese == "y":
#         print(Small_Pizza+Pepperoni_for_Small_Pizza+Extra_cheese_for_any_size_pizza)
#     elif Extra_addings == "y" and Extra_cheese == "n":
#         print(Small_Pizza+Pepperoni_for_Small_Pizza)
#     elif Extra_addings == "n" and Extra_cheese == "y":
#         print(Small_Pizza+Extra_cheese_for_any_size_pizza)
#     else:
#         print(Small_Pizza)

# elif pizza_size == 'M':
#     if Extra_addings == "y" and Extra_cheese == "y":
#         print(Medium_Pizza+Pepperoni_for_Small_Pizza+Extra_cheese_for_any_size_pizza)
#     elif Extra_addings == "y" and Extra_cheese == "n":
#         print(Medium_Pizza+Pepperoni_for_Small_Pizza)
#     elif Extra_addings == "n" and Extra_cheese == "y":
#         print(Medium_Pizza+Extra_cheese_for_any_size_pizza)
#     else:
#         print(Medium_Pizza)

# else:
#     pizza_size == 'L'
#     if Extra_addings == "y" and Extra_cheese == "y":
#         print(Large_Pizza+Pepperoni_for_Small_Pizza+Extra_cheese_for_any_size_pizza)
#     elif Extra_addings == "y" and Extra_cheese == "n":
#         print(Medium_Pizza+Pepperoni_for_Small_Pizza)
#     elif Extra_addings == "n" and Extra_cheese == "y":
#         print(Medium_Pizza+Extra_cheese_for_any_size_pizza)
#     else:
#         print(Medium_Pizza)

"""Using function"""
def Pizza_Prize(size):
    if pizza_size == 'S':
    if Extra_addings == "y" and Extra_cheese == "y":
        print(Small_Pizza+Pepperoni_for_Small_Pizza+Extra_cheese_for_any_size_pizza)
    elif Extra_addings == "y" and Extra_cheese == "n":
        print(Small_Pizza+Pepperoni_for_Small_Pizza)
    elif Extra_addings == "n" and Extra_cheese == "y":
        print(Small_Pizza+Extra_cheese_for_any_size_pizza)
    else:
        print(Small_Pizza)






