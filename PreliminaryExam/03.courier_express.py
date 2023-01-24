weight = float(input())
service_type = input()
distance = int(input())
if service_type == "standard":
    if weight < 1:
        price = distance * 0.03
    elif weight < 10:
        price = distance * 0.05
    elif weight < 40:
        price = distance * 0.10
    elif weight < 90:
        price = distance * 0.15
    elif weight < 150:
        price = distance * 0.20
else:
    if weight < 1:
        price = distance * 0.03 + distance * weight * 0.03 * 0.8
    elif weight < 10:
        price = distance * 0.05 + distance * weight * 0.05 * 0.4
    elif weight < 40:
        price = distance * 0.10 + distance * weight * 0.10 * 0.05
    elif weight < 90:
        price = distance * 0.15 + distance * weight * 0.15 * 0.02
    elif weight < 150:
        price = distance * 0.20 + distance * weight * 0.20 * 0.01
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
