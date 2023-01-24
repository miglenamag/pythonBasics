budget_film = float(input())
destination = input()
season = input()
number_of_days = int(input())
if destination == "Dubai":
    if season == "Winter":
        total_sum = number_of_days * 45000
    elif season == "Summer":
        total_sum = number_of_days * 40000
    total_sum *= 0.70
elif destination == "Sofia":
    if season == "Winter":
        total_sum = number_of_days * 17000
    elif season == "Summer":
        total_sum = number_of_days * 12500
    total_sum *= 1.25
elif destination == "London":
    if season == "Winter":
        total_sum = number_of_days * 24000
    elif season == "Summer":
        total_sum = number_of_days * 20250

diff = abs (total_sum - budget_film)
