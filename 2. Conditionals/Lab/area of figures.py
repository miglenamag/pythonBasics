from math import pi
figure = input()
area = 0
if figure == "square":
    side = float (input())
    area = side ** 2

elif figure == "rectangle":
    side = float (input())
    side_b = float(input())
    area = side * side_b
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height /2
elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2
print(f"{area:.3f}")
