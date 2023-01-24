# "The final price is: {крайна цена на услугата} lv."
#	"The discount is: {отстъпка} lv."
sq_meters=float(input())
total_sum=sq_meters*7.61

discount=total_sum*0.18

final_sum=total_sum-discount
print(f'The final price is: {final_sum} lv.')
print(f"The discount is: {discount} lv.")