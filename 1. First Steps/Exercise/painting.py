nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
total_sum = (nylon+2) * 1.50 + \
            paint * 1.1 * 14.50 +\
            thinner * 5 + 0.40
per_hour = total_sum * 0.3
sum_lab = per_hour * hours
total = total_sum + sum_lab
print(total)
