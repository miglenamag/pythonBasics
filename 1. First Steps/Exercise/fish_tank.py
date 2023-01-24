length = int(input())
width = int(input())
height = int(input())
percent = float(input())
total_volume = length * width * height / 1000
water = total_volume - total_volume * percent/100
print(water)