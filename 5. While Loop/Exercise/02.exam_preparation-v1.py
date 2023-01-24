number_low_scores = int(input())
counter_low_scores = 0
total_score = 0
number_problems = 0
is_end = False
last_problem_name = ""
while counter_low_scores  < number_low_scores:
    problem_name = input()
    if problem_name == "Enough":
        is_end = True
        break

    problem_score = int(input())
    if problem_score <= 4:
            counter_low_scores += 1
    number_problems += 1
    total_score += problem_score
    last_problem_name = problem_name


if is_end:
    if number_problems > 0:
        print (f" Average score: {total_score / (number_problems):.2f}")
        print(f"Number of problems: {number_problems}")
        print(f"Last problem: {last_problem_name}")

else:
    print(f"You need a break, {counter_low_scores} poor grades.")