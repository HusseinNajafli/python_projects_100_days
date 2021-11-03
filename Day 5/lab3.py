# The highest score in the class

# Input of scores
students_scores = input("Input a list of student scores: ").split()

for i in range(0, len(students_scores)):
    students_scores[i] = int(students_scores[i])

# Define the highets score
max_score = students_scores[0]students_scores = input("Input a list of student scores: ").split()

for i in range(0, len(students_scores)):
    students_scores[i] = int(students_scores[i])

# Define the highets score
max_score = students_scores[0]

# Find the the highest score
j = 0
for score in students_scores:
    j = j + 1
    if max_score < students_scores[j - 1]:
        max_score = students_scores[j - 1]

print(f"The highest score in the class is: {max_score}")