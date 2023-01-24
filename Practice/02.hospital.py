period = int(input())
total_examined = 0
total_unexamined = 0
doctors = 7
for day in range(1, period + 1):
    number_patients = int(input())
    if day % 3 == 0:
        if total_unexamined > total_examined:
            doctors += 1
    if number_patients < doctors:
            total_examined += number_patients
    elif number_patients >= doctors:
            total_examined += doctors
            total_unexamined += number_patients - doctors
print(f"Treated patients: {total_examined}.")
print(f"Untreated patients: {total_unexamined}.")
