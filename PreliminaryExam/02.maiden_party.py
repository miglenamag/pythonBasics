price_maiden_party = float(input())
numbers_love_messages = int(input())
numbers_roses = int(input())
numbers_keychains = int(input())
numbers_cartoons = int(input())
numbers_good_lucks = int(input())
total_numbers_goods = numbers_love_messages + numbers_roses + numbers_keychains + numbers_cartoons + numbers_good_lucks
earned_sum = numbers_love_messages * 0.60 + \
             numbers_roses * 7.20 + \
             numbers_keychains * 3.60 + \
             numbers_cartoons * 18.20 + \
             numbers_good_lucks * 22
if total_numbers_goods >= 25:
    earned_sum *= 0.65
earned_sum *= 0.90
difference = abs(price_maiden_party - earned_sum)

if earned_sum >= price_maiden_party:
    print (f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
