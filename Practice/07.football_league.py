capacity = int(input())
fans = int(input())
fans_A = 0
fans_B = 0
fans_V = 0
fans_G = 0
for i in range(1, fans + 1):
    sector = input()
    if sector == "A":
        fans_A += 1
    elif sector == "B":
        fans_B += 1
    elif sector == "V":
        fans_V += 1
    elif sector == "G":
        fans_G += 1
percent_A = fans_A / fans * 100
percent_B = fans_B / fans * 100
percent_V = fans_V / fans * 100
percent_G = fans_G / fans * 100
percent_all_fans = fans / capacity * 100
print(f"{percent_A:.2f}%")
print(f"{percent_B:.2f}%")
print(f"{percent_V:.2f}%")
print(f"{percent_G:.2f}%")
print(f"{percent_all_fans:.2f}%")



