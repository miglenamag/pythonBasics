total_steps = 0
daily_steps = 0
while total_steps < 10000:
    command = input()
    if command != "Going home":
        daily_steps = int(command)
        total_steps += daily_steps
    else:
        daily_steps = int(input())
        total_steps += daily_steps
        break
difference = abs(10000 - total_steps)
if total_steps < 10000:
    print(f"{difference} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
