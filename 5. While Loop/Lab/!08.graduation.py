student_name = input()

sum = 0
year = 1
fail_counter = 0
while year <= 12:
    if fail_counter > 1:
        break
    grade = float(input())
    if grade < 4.00:
        fail_counter += 1
        continue
    sum += grade
    year += 1

if fail_counter > 1:
    print(f"{student_name} has been excluded at {year} grade")
else:
    print(f"{student_name} graduated. Average grade: {sum / 12:.2f}")
