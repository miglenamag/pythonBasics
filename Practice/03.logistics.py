number_loads = int(input())
total_load = 0
total_price = 0
cargo_bus = 0
cargo_train = 0
cargo_track = 0
for i in range(1, number_loads + 1):
    weight_load = int(input())
    total_load += weight_load
    if weight_load <= 3:
        total_price += weight_load * 200
        cargo_bus += weight_load
    elif 4 <= weight_load <= 11:
        total_price += weight_load * 175
        cargo_track += weight_load
    elif weight_load >= 12:
        total_price += weight_load * 120
        cargo_train += weight_load
average_price_per_ton = total_price / total_load
percent_cargo_bus = cargo_bus / total_load * 100
percent_cargo_truck = cargo_track / total_load * 100
percent_cargo_train = cargo_train / total_load * 100
print(f"{average_price_per_ton:.2f}")
print(f"{percent_cargo_bus:.2f}%")
print(f"{percent_cargo_truck:.2f}%")
print(f"{percent_cargo_train:.2f}%")