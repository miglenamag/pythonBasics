score = int(input())
if score < 100:
    bon_score = 5
elif score > 1000:
    bon_score = score * 0.1
else:
    bon_score = score * 0.2
if score % 2 == 0:
    bon_score += 1
elif score % 10 == 5:
    bon_score += 2
print(bon_score)
print(score + bon_score)
