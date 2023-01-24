command = input()
current_height = 0
total_height = 5364
days = 1
while command != "END":
    current_height = int(input())
    if total_height < 8848:
        if command == "Yes":
            days = days + 1
        if days == 5:
            total_height += current_height
            break
    total_height += current_height
    if total_height >= 8848:
        break
    command = input()
if total_height >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed")
    print(total_height)

