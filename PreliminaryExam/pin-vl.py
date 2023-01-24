max_first = int(input())
max_second = int(input())
max_third = int(input())
for first in range(2,max_first+1,2):
    for second in range(2,max_second+1):
        is_prime = True
        for i in range(2,second):
            if second%i==0:
                is_prime = False
                break
        if is_prime:
            for third in range(2,max_third+1,2):
                print(f"{first} {second} {third}")