#Finding average of students using loops
students_heights = [180, 124, 165, 173, 189, 169, 146]
sum = 0
count = 0
for student_height in students_heights:
    sum += student_height 
    count += 1
result = sum/count
#result = sum/len(students_heights)
print(round(result))
    