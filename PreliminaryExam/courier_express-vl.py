weight = float(input())
service = input()
distance = int(input())
if service == 'standard':
    if weight < 1:
        price = distance * 0.03
    elif weight < 10:
        price = distance * 0.05
    elif weight < 40:
        price = distance * 0.1
    elif weight < 90:
        price = distance * 0.15
    else:
        price = distance * 0.2
else:
    if weight < 1:
        price = distance * 0.03 + weight * distance * 0.03 * 0.8
    elif weight < 10:
        price = distance * 0.05 + weight * distance * 0.05 * 0.4
    elif weight < 40:
        price = distance * 0.1 + weight * distance * 0.1 * 0.05
    elif weight < 90:
        price = distance * 0.15 + weight * distance * 0.15 * 0.02
    else:
        price = distance * 0.2 + weight * distance * 0.2 * 0.01
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")