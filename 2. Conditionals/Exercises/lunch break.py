import math
name_of_serial = input()
duration_of_ep = int(input())
duration_of_break = int(input())
free = duration_of_break - duration_of_break/8 - duration_of_break/4
dif = abs(free - duration_of_ep)
dif = math.ceil(dif)
if free >= duration_of_ep:
    print(f"You have enough time to watch {name_of_serial} and left with {dif} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {dif} more minutes.")