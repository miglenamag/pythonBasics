number_pc = int(input())
total_sales = 0
total_rating = 0
for n in range(number_pc):
    number = int(input())
    rating = number % 10
    total_rating += rating
    posiible_sales = number // 10
    if rating == 3:
        total_sales += 0.5 * posiible_sales
    elif rating == 4:
        total_sales += 0.7 * posiible_sales
    elif rating == 5:
        total_sales += 0.85 * posiible_sales
    elif rating == 6:
        total_sales += posiible_sales
    else:
       total_sales += 0
avg_rating = total_rating / number_pc
print(f"{total_sales:.2f}")
print(f"{avg_rating:.2f}")
