student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
max = 0
for i in range(len(student_scores)-1):
    if student_scores[i+1] > max:
        max = student_scores[i+1]
print(max)