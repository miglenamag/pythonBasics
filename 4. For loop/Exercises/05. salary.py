number_of_tabs = int(input())
salary = float(input())
web_name = ""
for number in range(1, number_of_tabs + 1):
    web_name = input()
    if web_name == "Facebook":
        salary -= 150
    elif web_name == "Instagram":
        salary -= 100
    elif web_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(int(salary))
else:
    print ("You have lost your salary.")


