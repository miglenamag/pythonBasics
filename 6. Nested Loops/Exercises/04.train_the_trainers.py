number_of_jury = int(input())
name_of_presentation = input()
average_score_presentation = 0
counter_presentations = 0
current_score = 0
total_score = 0
while name_of_presentation != "Finish":
    counter_presentations += 1
    for counter in range(number_of_jury):
        jury_score = float(input())
        current_score += jury_score
    average_score_presentation = current_score / number_of_jury
    total_score += current_score
    print(f"{name_of_presentation} - {average_score_presentation:.2f}.")
    current_score = 0
    name_of_presentation = input()

average_total_score = total_score / (counter_presentations * number_of_jury)
print(f"Student's final assessment is {average_total_score:.2f}.")
