number_low_scores = int(input())
problem_name = ""
counter_low_scores = 0
total_score = 0
number_problems = 0
is_end = False
last_problem_name = ""
problem_score = 0
while problem_name != "Enough":
    last_problem_name = problem_name
    problem_name = input()
    if problem_name == "Enough":
        break
    problem_score = int(input())
    if problem_score <= 4:
        counter_low_scores += 1
    if counter_low_scores < number_low_scores:
        number_problems += 1
        total_score += problem_score
    else:
        is_end = True
        break
if is_end:
    print(f"You need a break, {counter_low_scores} poor grades.")
else:
    if number_problems > 0:
        print (f" Average score: {total_score / (number_problems):.2f}")
        print(f"Number of problems: {number_problems}")
        print(f"Last problem: {last_problem_name}")