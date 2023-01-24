width = int(input())
length = int(input())
area = width * length
pieces = 0
while area > 0:
    command = input()
    if command != 'STOP':
        pieces = int(command)
        area -= pieces
    else:
        break
if area>0:
    print(f"{area} pieces are left.")
else:
    area = abs(area)
    print(f"No more cake left! You need {area} pieces more.")