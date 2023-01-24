# step = int(input())
# start = int(input())
# end = int(input())
# for i in range(start, end, step):
#     print(i)

# for number in range(start,end):
# # start - inclusive
# # end - exclusive
# Когато ни интересува стойността на променливата number и как тя се променя се използва горния синтакис

# for i in range(end): # we are interested in number of iterations of loop iterations
# if 0<= i < end
# for e равносилен на if проверка
# когато не ни интересува как се променя променливата i и не следим нейната промяна във времето
# , а ни интересуват само броя итерации, задаваме само крайна стойност
# по подразбиране началната стойност е 0
# for i in range(11)
# print ("Hello)

# 1 стойност в range - end -# по подразбиране началната стойност е 0
# 2 стойности в range - start, end ----step по подразбиране е 1
# 3 стойности - start, end, step

# step може да бъде отрицателно число
# for number in range (20, 1, -2):
for number in range(1, 10):
    print (number)
    number += 100 # това не влияе върху брояча на цикъла и той се изпълнява целия
    # , докато се изпълнят всички итерации
    print(number)
