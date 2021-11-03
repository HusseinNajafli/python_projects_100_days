students_scores = input("Input a list of student scores: ").split()

for i in range(0, len(students_scores)):
    students_scores[i] = int(students_scores[i])

# Define the highets score
max_score = 0

for score in students_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")