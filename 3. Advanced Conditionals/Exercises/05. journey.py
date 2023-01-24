budget = float(input())
season = input()
destination = " "
is_hotel = False
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.30
    else:
        budget *= 0.70
        is_hotel = True

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.40
    else:
        budget *= 0.80
        is_hotel = True

else:
    destination = "Europe"
    budget *= 0.90
    is_hotel = True

print(f"Somewhere in {destination}")
if is_hotel:
    print(f"Hotel - {budget:.2f}")
else:
    print(f"Camp - {budget:.2f}")


