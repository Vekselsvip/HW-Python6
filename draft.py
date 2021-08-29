list = [0, 5, 2, 4, 7, 1, 3, 19]
list2 = []
for i in list:
    if i % 2 != 0:
        list2.append(i)
print(len(list2))