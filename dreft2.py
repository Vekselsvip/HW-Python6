list = []
for i in range(100):
    if i % 7 == 0:
        list.append(i)
    print(list)

    x = int(input('x= '))
    list = []
    for i in range(x):
        list.append(i + 1)
    summa = 1
    for j in list:
        summa = summa * j
        print(summa)

        x = int(input('x='))
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in list:
            y = i * x
            print(i, 'x', y)


list = [0, 5, 2, 4, 7, 1, 3, 19]
list2 = []
for i in list:
    if i % 2 != 0:
        list2.append(i)
print(len(list2))