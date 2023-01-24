command = input()
total = 0
while command != "NoMoreMoney":
    curr_sum = float(command)
    if curr_sum >= 0:
        print(f"Increase: {curr_sum:.2f}")
        total += curr_sum
    else:
        print("Invalid operation!")
        break
    command = input()
print(f"Total: {total:.2f}")