type_flowers = input()
number_flowers = int(input())
budget = int(input())
current_budget = 0
diff = 0
# is_condition = True
if type_flowers == "Roses":
    current_budget = number_flowers * 5
    if number_flowers > 80:
        current_budget *= 0.90
    # else:
    #     is_condition == False
    diff = abs(current_budget - budget)

elif type_flowers == "Dahlias":
    current_budget = number_flowers * 3.80
    if number_flowers > 90:
        current_budget *= 0.85
    # else:
    #     is_condition == False
    diff = abs(current_budget - budget)

elif type_flowers == "Tulips":
    current_budget = number_flowers * 2.80
    if number_flowers > 80:
        current_budget *= 0.85
    # else:
    #     is_condition == False
    diff = abs(current_budget - budget)

elif type_flowers == "Narcissus":
    current_budget = number_flowers * 3.00
    if number_flowers < 120:
        current_budget *= 1.15
    # else:
    #     is_condition == False
    diff = abs(current_budget - budget)

elif type_flowers == "Gladiolus":
    current_budget = number_flowers * 2.50
    if number_flowers < 80:
        current_budget *= 1.20
    # else:
    #     is_condition == False
    diff = abs(current_budget - budget)

# if is_condition:
if current_budget <= budget:
        print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
        print(f"Not enough money, you need {diff:.2f} leva more.")