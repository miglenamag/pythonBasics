number_groups = int(input())
number_people_in_group = 0
total_number_people = 0
people_musala = 0
people_monblan = 0
people_kiliman = 0
people_k2 = 0
people_everest = 0
for number in range(number_groups):
    number_people_in_group = int(input())
    total_number_people += number_people_in_group
    if number_people_in_group <= 5:
        people_musala += number_people_in_group
    elif number_people_in_group < 13:
        people_monblan += number_people_in_group
    elif number_people_in_group < 26:
        people_kiliman += number_people_in_group
    elif number_people_in_group < 41:
        people_k2 += number_people_in_group
    else:
        people_everest += number_people_in_group
print(f"{people_musala / total_number_people * 100:.2f}%")
print(f"{people_monblan / total_number_people * 100:.2f}%")
print(f"{people_kiliman/ total_number_people * 100:.2f}%")
print(f"{people_k2 / total_number_people * 100:.2f}%")
print(f"{people_everest / total_number_people * 100:.2f}%")
