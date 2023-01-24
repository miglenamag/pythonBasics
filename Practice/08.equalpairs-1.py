number_pairs = int(input())
sum_pairs = 0
diff_pairs = 0
max_diff = 0
equal = True
for i in range(1, number_pairs + 1):
    element1 = int(input())
    element2 = int(input())
    curr_sum_pairs = element1 + element2
    if curr_sum_pairs != sum_pairs:
        if sum_pairs != 0:
            diff_pairs =abs(curr_sum_pairs - sum_pairs)
        sum_pairs = curr_sum_pairs
        if diff_pairs > max_diff:
            max_diff = diff_pairs
            equal = False
if equal:
    print(f"Yes, value={sum_pairs}")
else:
    print(f"No, maxdiff={max_diff}")
