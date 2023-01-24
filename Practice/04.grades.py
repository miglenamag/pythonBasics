number_students = int(input())
av_grade = 0
number_fail = 0
number_middle = 0
number_good = 0
number_top = 0
for i in range(1, number_students + 1):
    grade = float(input())
    if 2 <= grade <= 2.99:
        number_fail += 1
    elif 3 <= grade <= 3.99:
        number_middle += 1
    elif 4 <= grade <= 4.99:
        number_good += 1
    elif grade >= 5:
        number_top += 1
    av_grade += grade
av_grade /= number_students
percent_fail = number_fail / number_students * 100
percent_middle = number_middle / number_students * 100
percent_good = number_good / number_students * 100
percent_top = number_top / number_students * 100
print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_middle:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {av_grade:.2f}")
