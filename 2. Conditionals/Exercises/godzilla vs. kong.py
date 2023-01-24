budget = float(input())
num_stat = int(input())
price = float(input())
needed_sum = budget * 0.1 + num_stat * price
if num_stat > 150:
    needed_sum -= num_stat * price * 0.1
dif = abs(budget - needed_sum)
if needed_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {dif:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {dif:.2f} leva left.")
