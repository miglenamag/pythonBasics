number_of_computers = int(input())
sold = 0
average_rating = 0
for i in range(number_of_computers):
    number = int(input())
    rating = number % 10
    average_rating += rating
    if rating == 3:
        sold += number // 10 * 0.5
    elif rating == 4:
        sold += number // 10 * 0.7
    elif rating == 5:
        sold += number // 10 * 0.85
    elif rating == 6:
        sold += number // 10
average_rating /= number_of_computers
print(f"{sold:.2f}")
print(f"{average_rating:.2f}")
