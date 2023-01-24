import sys
n = int(input())
sum = 0
max_num = -sys.maxsize
diff = 0
for i in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum += current_num
if max_num == sum - max_num:
    print("Yes ")
    print(f"Sum = {max_num}")
else:
    sum_others = sum - max_num
    diff = abs(max_num-sum_others)
    print("No")
    print(f"Diff = {diff}")




