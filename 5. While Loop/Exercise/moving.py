width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
box = 0
while total_space > 0:
    command = input()
    if command != 'Done':
        box = int(command)
        total_space -= box
    else:
        break
if total_space > 0:
    print(f"{total_space} Cubic meters left.")
else:
    total_space = abs(total_space)
    print(f"No more free space! You need {total_space} Cubic meters more.")