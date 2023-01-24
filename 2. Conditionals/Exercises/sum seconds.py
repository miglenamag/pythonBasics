first = int(input())
second = int(input())
third = int(input())
total_minutes = (first + second + third) // 60
total_seconds = (first + second + third) % 60
print (f"{total_minutes}:{total_seconds:02d}")



