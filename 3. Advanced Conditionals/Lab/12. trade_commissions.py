town = input()
sales = float(input())
invalid = False
comission = 0
if town == "Sofia":
    if 0 <= sales <= 500:
        comission = 0.05 * sales
    elif 500 < sales <= 1000:
        comission = 0.07 * sales
    elif 1000 < sales <= 10000:
        comission = 0.08 * sales
    elif sales > 10000:
        comission = 0.12 * sales
    else:
        invalid = True
elif town == "Varna":
    if 0 <= sales <= 500:
        comission = 0.045 * sales
    elif 500 < sales <= 1000:
        comission = 0.075 * sales
    elif 1000 < sales <= 10000:
        comission = 0.10 * sales
    elif sales > 10000:
        comission = 0.13 * sales
    else:
        invalid = True
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        comission = 0.055 * sales
    elif 500 < sales <= 1000:
        comission = 0.08 * sales
    elif 1000 < sales <= 10000:
        comission = 0.12 * sales
    elif sales > 10000:
        comission = 0.145 * sales
    else:
        invalid = True
else:
    invalid = True

if invalid:
    print("error")
else:
    print(f"{comission:.2f}")
