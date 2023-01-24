record = float(input())
distance = float(input())
seconds_per_meter = float(input())
delay = distance // 15 * 12.5
current_record = distance * seconds_per_meter + delay
dif = abs(current_record - record)
if current_record >= record:
    print(f"No, he failed! He was {dif:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {current_record:.2f} seconds.")
