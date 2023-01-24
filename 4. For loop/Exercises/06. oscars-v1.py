name_of_actor = input()
academy_points = float(input())
number_of_assessors = int(input())
total_points = academy_points
name_of_assessor = ""
assessor_points = 0

for number in range(number_of_assessors):
    name_of_assessor = input()
    assessor_points = float(input())
    total_points += len(name_of_assessor) * assessor_points / 2
    difference_points = abs(total_points - 1250.5)
    if total_points > 1250.5:
        break
if total_points < 1250.5:
    print (f"Sorry, {name_of_actor} you need {difference_points:.1f} more!")
else:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
