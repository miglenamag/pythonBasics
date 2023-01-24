months = int(input())
total_el = 0
total_other = 0
for period in range(1, months+1):
    el_expences = float(input())
    total_el += el_expences
    other_expences = (el_expences + 20 + 15) * 1.2
    total_other += other_expences
total_water = period * 20
total_inet = period * 15
total_expenses = total_el + total_water + total_inet + total_other
avg_expenses = total_expenses / period
print(f"Electricity: {total_el:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_inet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {avg_expenses:.2f} lv")
