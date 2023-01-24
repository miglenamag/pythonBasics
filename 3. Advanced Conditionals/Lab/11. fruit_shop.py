fruit = input()
weekday = input()
quantity = float (input())

price = 0
invalid = False
working_day = weekday == "Monday" or \
              weekday == "Tuesday" or \
              weekday == "Wednesday" or \
              weekday == "Thursday" or \
              weekday == "Friday"
weekend = weekday == "Saturday" or weekday == "Sunday"
if working_day:
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity *1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity *2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        invalid = True
elif weekend:
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity *1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20
    else:
        invalid = True
else:
    invalid = True

if invalid:
    print ("error")
else:
    print(f" {price:.2f}")