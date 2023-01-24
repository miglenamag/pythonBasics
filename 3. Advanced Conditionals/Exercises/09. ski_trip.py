days = int(input())
type_of_room = input()
evaluation = input()
total_price = 0

if type_of_room == "apartment":
    if days < 10:
        total_price = (days -1) * 25 * 0.7
    elif 10 <= days <= 15:
        total_price = (days - 1) * 25 * 0.65
    else:
        total_price = (days - 1) * 25 * 0.50
elif type_of_room == "president apartment":
    if days < 10:
        total_price = (days -1) * 35 * 0.9
    elif 10 <= days <= 15:
        total_price = (days - 1) * 35 * 0.85
    else:
        total_price = (days - 1) * 35 * 0.80
else:
    total_price = (days - 1) * 18
if evaluation == "positive":
    total_price+=total_price*0.25
else:
    total_price-=total_price*0.10
print(f'{total_price:.2f}')

