# Депозирана сума – реално число в интервала [100.00 … 10000.00]
# Срок на депозита (в месеци) – цяло число в интервала [1…12]
# Годишен лихвен процент – реално число в интервала [0.00 …100.00]

sum = float(input())
term = int(input())
interest_rate = float(input())
sum_annual = sum * interest_rate / 100
interest_rate_month = sum_annual / 12
total_sum = sum + term * interest_rate_month

print(total_sum)
