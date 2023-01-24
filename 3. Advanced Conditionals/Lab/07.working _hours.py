hour = int(input())
day = input()
work_day = day != "Sunday"
work_hour = 10 <= hour <= 18
if work_day:
    if work_hour:
        print("open")
    else:
        print("closed")
else:
    print("closed")