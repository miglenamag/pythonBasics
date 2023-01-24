start = int(input())
end = int(input())
magic = int(input())
combination_counter = 0
is_found = False
for i in range(start, end+1):
    if is_found:
        break
    for j in range(start, end+1):
        combination_counter += 1
        if i + j == magic:
            first = i
            second = j
            is_found = True
            if is_found:
                break
if is_found:
        print(f" Combination N:{combination_counter} ({first} + {second} = {magic})")
else:
    print(f"{combination_counter} combinations - neither equals {magic}")