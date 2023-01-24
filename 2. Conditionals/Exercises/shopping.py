budget = float(input())
video_cards = int(input())
cpu = int(input())
ram = int(input())
price_video_cards = 250
price_cpu = video_cards * price_video_cards * 0.35
price_ram = video_cards * price_video_cards * 0.1
total_sum = video_cards * price_video_cards + cpu * price_cpu + ram * price_ram
if video_cards > cpu:
    total_sum *= 0.85
dif = abs(total_sum - budget)
if total_sum <= budget:
    print(f"You have {dif:.2f} leva left!")
else:
    print(f"Not enough money! You need {dif:.2f} leva more!")
