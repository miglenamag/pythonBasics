number1 = int(input())
number2 = int(input())
operation = input()
result = 0
type_operation = operation == "+" or operation == "-" or operation == "*"
if type_operation:
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    if result % 2 == 0:
        print(f"{number1} {operation} {number2} = {result} - even")
    else:
        print(f"{number1} {operation} {number2} = {result} - odd")
else:
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        if operation == "/":
           result = number1 / number2
           print(f"{number1} / {number2} = {result:.2f}")
        elif operation == "%":
           result = number1 % number2
           print(f"{number1} % {number2} = {result}")


