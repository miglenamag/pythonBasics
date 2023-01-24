type_projection = input()
rows = int(input())
columns = int(input())
price_per_ticket = 0
if type_projection == "Premiere":
    price_per_ticket = 12.00
elif type_projection == "Normal":
    price_per_ticket = 7.50
else:
    price_per_ticket = 5.00
total = rows * columns * price_per_ticket
print (f"{total:.2f} leva")


