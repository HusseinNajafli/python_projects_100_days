student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0

# OR
# for i in range(len(student_heights)):
#     total += student_heights[i]

for height in student_heights:
    total = total + height

# number_of_students = len(student_heights)
# OR
number_of_students = 0
for student in student_heights:
    number_of_students += 1
    
average = round(total / number_of_students)

# OR
# total = sum(student_heights) 

# OR
# average = round(total / len(student_heights))

print(average)
