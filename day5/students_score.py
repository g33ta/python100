students_scores = input('Enter list of students score ')
#have to convert string numbers to list with integers.
splited_list = students_scores.split( )
listed_score = []
for score in splited_list:
    listed_score.append(int(score))
print(listed_score)
#Finding maximum score.
max_num = 0
for scr in listed_score:
    if max_num<scr:
        max_num = scr
print('The highest score in the class is:',max_num)

"""Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/DnSPgYNSTgeHRJ3MinHg"""

