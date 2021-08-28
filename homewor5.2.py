n = int(input('n='))
list = []
for i in range(n):
    list.append(i + 1)
summa = 1
for j in list:
    summa *= j
print(summa)