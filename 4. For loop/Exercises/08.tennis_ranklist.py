import math

number_of_tourneys = int(input())
start_points = int(input())
stage_of_tourney = ""
total_points = start_points
earned_points = 0
number_of_earned_tourneys = 0
for num in range(number_of_tourneys):
    stage_of_tourney = input()
    if stage_of_tourney == "W":
        total_points += 2000
        earned_points += 2000
        number_of_earned_tourneys += 1
    elif stage_of_tourney == "F":
        total_points += 1200
        earned_points += 1200
    else:
        total_points += 720
        earned_points += 720
average_points = math.floor(earned_points / number_of_tourneys)
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{number_of_earned_tourneys / number_of_tourneys * 100:.2f}%")

