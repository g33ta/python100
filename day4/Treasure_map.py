row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

rows = [row1,row2,row3]
position = input("Where do you want to put the treasure?x,y ") 
integer = map(int,position) #converted string to integer.
listed_num = list(integer) #converted integer to list

column = listed_num[0]
row = listed_num[1]
rows[column][row] = 'x'# 
print(f"{row1}\n{row2}\n{row3}")


#Her code
rows = [row1,row2,row3]
position = input("Where do you want to put the treasure?x,y ") 
column = int(position[0])
row = int(position[1])
rows[column][row] = 'x'# 
print(f"{row1}\n{row2}\n{row3}")

"""Instructions
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list.
When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
This is to try and simulate the coordinates on a real map.


Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:

23
Example Output 1
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']"""
