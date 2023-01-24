steps = int(input())
num_to9 = 0
num_to19 = 0
num_to29 = 0
num_to39 = 0
num_to50 = 0
points = 0
invalid = 0
for i in range(steps):
    number = int(input())
    if 0 <= number <= 50:
        if 0 <= number <= 9:
            num_to9 += 1
            points += 0.2 * number
        elif 10 <= number <= 19:
            num_to19 += 1
            points += 0.3 * number
        elif 20 <= number <= 29:
            num_to29 += 1
            points += 0.4 * number
        elif 30 <= number <= 39:
            num_to39 += 1
            points += 50
        elif 40 <= number <= 50:
            num_to50 += 1
            points += 100
    else:
        invalid += 1
        points = points / 2
print(f"{points:.2f}")
print(f"From 0 to 9: {(num_to9 / steps * 100):.2f}%")
print(f"From 10 to 19: {(num_to19 / steps * 100):.2f}%")
print(f"From 20 to 29: {(num_to29 / steps * 100):.2f}%")
print(f"From 30 to 39: {(num_to39 / steps * 100):.2f}%")
print(f"From 40 to 50: {(num_to50 / steps * 100):.2f}%")
print(f"Invalid numbers: {(invalid / steps * 100):.2f}%")
