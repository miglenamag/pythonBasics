month = input()
nights = int(input())
total_price_studio = 0
total_price_apartment = 0
price_per_night_studio = 0
price_per_night_apartment = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65
    total_price_studio = price_per_night_studio * nights
    total_price_apartment = price_per_night_apartment * nights
    if 7 < nights <= 14:
        total_price_studio *= 0.95
    elif nights > 14:
        total_price_studio *= 0.70

elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
    total_price_studio = price_per_night_studio * nights
    total_price_apartment = price_per_night_apartment * nights
    if  nights > 14:
        total_price_studio *= 0.80

elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apartment = 77
    total_price_studio = price_per_night_studio * nights
    total_price_apartment = price_per_night_apartment * nights

if  nights > 14:
        total_price_apartment *= 0.90

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")

