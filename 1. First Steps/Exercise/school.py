num_pen = int (input())
num_marker = int (input())
liter = int(input())
disc_percent = int(input())
total_pens = num_pen * 5.80
total_markers = num_marker * 7.20
liquid = liter * 1.20
total_sum_disc = (total_pens + total_markers + liquid) * disc_percent / 100
total =float ((total_pens + total_markers + liquid) - total_sum_disc)
print (f'На Ани са нужни {total} лв., за да плати сметката')