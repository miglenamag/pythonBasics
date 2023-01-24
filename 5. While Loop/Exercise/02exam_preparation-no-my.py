number_low_scores = int(input())
problem_name = input()
counter_low_scores = 0
total_score = 0
number_problems = 1
is_end = False
last_problem_name = problem_name
while problem_name != "Enough":
    last_problem_name = problem_name
    problem_score = int(input())
    if problem_score <= 4:
        if counter_low_scores != number_low_scores:
            counter_low_scores += 1
            number_problems += 1
            total_score += problem_score
            problem_name = input()
        else:
            is_end = True
            break

if is_end:
    print (f"You need a break, {counter_low_scores} poor grades.")
else:
    print (f" Average score: {total_score / (number_problems - 1):.2f}")
    print(f"Number of problems: {number_problems-1}")
    print(f"Last problem: {last_problem_name}")