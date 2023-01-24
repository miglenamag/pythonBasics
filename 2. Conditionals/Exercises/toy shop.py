ex_price = float(input())
num_puzzs = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())
toys = num_trucks + num_puzzs + num_minions + num_bears + num_dolls
total_sum = num_puzzs * 2.60 + \
            num_dolls * 3 + \
            num_bears * 4.10 + \
            num_minions * 8.20 + \
            num_trucks * 2
if toys >= 50:
    # total_sum -= total_sum * 0.25
    total_sum *= 0.75
total_sum *= 0.90
diference = abs(total_sum - ex_price)
if total_sum >= ex_price:
    print(f"Yes! {diference :.2f} lv left.")
else:
    print(f"Not enough money! {diference :.2f} lv needed.")
