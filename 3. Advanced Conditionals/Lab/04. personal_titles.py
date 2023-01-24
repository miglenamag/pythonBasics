age = float(input())
sex = input()
if age >= 16:
    if sex == "f":
        print("Ms.")
    else:
        print("Mr.")

else:
    if sex == "f":
        print("Miss")
    else:
        print("Master")
