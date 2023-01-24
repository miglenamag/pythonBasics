import math
days = int(input())
left_food = int(input())
food_per_day_first = float(input())
food_per_day_second = float(input())
food_per_day_third = float(input())
needed_food = days*(food_per_day_first+food_per_day_second+food_per_day_third)
diff = abs(needed_food - left_food)
if left_food >= needed_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")






