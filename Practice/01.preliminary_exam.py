people = int(input())
nigths = int(input())
cards_per_person = int(input())
museums_per_person = int(input())
sum = people * (nigths*20 + cards_per_person*1.60 + museums_per_person*6)
sum += sum*0.25
print (f"{sum:.2f}")
