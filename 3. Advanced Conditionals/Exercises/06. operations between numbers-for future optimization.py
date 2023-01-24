number1 = int(input())
number2 = int(input())
operation = input()
result = 0
printed_only_result = False
err_flag = False
if operation == "+" or operation == "-" or operation == "*":
    operation = operation[0]
    print(operation)
    # result = number1 {operation} number2
    # # if result % 2 == 0:
    #     print (f"{number1} {operation} {number2} = {result} - even")
    # else:
    #     print(f"{number1} {operation} {number2} = {result} - odd")

# elif operation == "/":
#     if number2 != 0:
#         result = number1 / number2
#         printed_only_result = True
#     else:
#         err_flag = True
#
# elif operation == "%":
#     result = number1 % number2
#     printed_only_result = True
#
# if printed_only_result:
#     if not err_flag:
#         print (f"{number1} {operation} {number2} = {result}")
#     else:
#         print(f"Cannot divide {number1} by zero")