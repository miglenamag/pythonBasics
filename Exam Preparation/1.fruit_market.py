strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())
raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2
total_price = banana_quantity * banana_price + \
              orange_quantity * orange_price + \
              raspberry_price * raspberry_price + \
              strawberry_quantity * strawberry_price
print (f"{total_price:.2f}")
