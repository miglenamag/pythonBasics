money = float(input())
money = int(money * 100)
change = money // 200
money %= 200
change += money // 100
money %= 100
change += money // 50
money %= 50
change += money // 20
money %= 20
change += money // 10
money %= 10
change += money // 5
money %= 5
change += money // 2
money %= 2
change += money // 1
money %= 1
print(change)
