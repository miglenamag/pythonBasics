age = int(input())
wash_price = float(input())
toy_price = int(input())
toys = 0
bday_money = 0
total_money = 0
for current_age in range(1, age + 1):
    if current_age % 2 != 0:
        toys += 1
    else:
        bday_money += 10
        total_money += bday_money - 1
total_money += toys * toy_price
difference = abs(total_money - wash_price)
if total_money >= wash_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
