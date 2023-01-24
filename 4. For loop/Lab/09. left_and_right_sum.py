number = int(input())
sumleft = 0
sumright = 0
for i in range(number):
    sumleft = sumleft + int(input())
for i in range(number ):
    sumright = sumright + int(input())
diff = abs(sumleft - sumright)
if sumright == sumleft:
    print(f" Yes, sum = {sumleft}")
else:
    print(f" No, diff = {diff}")




