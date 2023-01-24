our_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())
time_exam = hour_exam * 60 + minutes_exam
time_arrival = hour_arrival * 60 + minutes_arrival
if time_arrival > time_exam:
    print("Late")
elif time_exam - 30 <= time_arrival <= time_exam:
    print("On time")
else:
    print("Early")
diff = abs(time_arrival - time_exam)
hours = diff // 60
minutes = diff % 60
if time_exam - 60 < time_arrival < time_exam:
    print(f"{minutes} minutes before the start")
elif time_arrival <= time_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_arrival < time_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_arrival  >= time_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")