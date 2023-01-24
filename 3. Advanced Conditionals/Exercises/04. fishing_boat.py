# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.
budget = int(input())
season = input()
number_fishers = int(input())
current_rent = 0
diff = 0
if season == "Spring":
    current_rent = 3000
elif season == "Winter":
    current_rent = 2600
else:
    current_rent = 4200
if number_fishers <= 6:
    current_rent *= 0.90
elif number_fishers <= 11:
    current_rent *= 0.85
else:
    current_rent *= 0.75
if number_fishers % 2 == 0 and season != "Autumn":
    current_rent *= 0.95
diff = abs(current_rent - budget)
if current_rent <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
