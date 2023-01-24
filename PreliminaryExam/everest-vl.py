command = input()
total_height = 5364
days = 1
while command != 'END':
    metres = int(input())
    if command == 'Yes':
        days += 1
    if days > 5:
        break
    total_height += metres
    if total_height >= 8848:
        break
    command = input()
if total_height >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(str(total_height))
