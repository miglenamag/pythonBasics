money = float(input())
year = int(input())
rest_sum = money
age = 17
for i in range(1800, year + 1):
    age += 1
    if i % 2 == 0:
        rest_sum -= 12000
    else:
        rest_sum -= 12000 + 50 * age
if rest_sum >=0:
    print(f"Yes! He will live a carefree life and will have {rest_sum:.2f} dollars left.")
else:
    print(f"He will need {abs(rest_sum):.2f} dollars to survive.")
