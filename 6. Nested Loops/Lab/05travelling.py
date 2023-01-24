destination = input()
budget = float(input())
sum = 0
is_going = False
while destination != "End":
        current_sum = float(input())
        sum += current_sum
        if sum > budget:
            is_going = True
            print(f"Going to {destination}!")
            sum = 0
            destination = input()
            if destination != "End":
                budget = float(input())


