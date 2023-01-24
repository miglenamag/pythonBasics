end_first_digit = int(input())
end_second_digit = int(input())
end_third_digit = int(input())
for first_digit in range(2, end_first_digit + 1, 2):
    for second_digit in range(2, end_second_digit + 1):
        is_prime = True
        for i in range(2, second_digit):
            if second_digit % i == 0:
                is_prime = False
                break
        if is_prime:
                for third_digit in range(2, end_third_digit + 1, 2):
                    print (f"{first_digit} {second_digit} {third_digit}")



