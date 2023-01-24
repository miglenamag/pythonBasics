percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())
fats_weight = ((total_calories * percent_fats) / 100) / 9
proteins_weights = ((total_calories * percent_proteins) / 100) / 4
carbohydrates_weight = ((total_calories * percent_carbohydrates) / 100) / 4
total_weight_food = fats_weight + proteins_weights + carbohydrates_weight
total_calories_per_gr = total_calories / total_weight_food
net_percent_water = 100 - percent_water
net_calories_per_gr = (total_calories_per_gr * net_percent_water) / 100
print (f"{net_calories_per_gr:.4f}")
