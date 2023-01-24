num_chicken = int(input())
num_fish = int(input())
num_veg = int(input())
pr_chicken = 10.35
pr_fish = 12.40
pr_veg = 8.15
total = num_chicken * pr_chicken + \
        num_fish * pr_fish + \
        num_veg * pr_veg
final = total * 1.20 + 2.50
print(final)


