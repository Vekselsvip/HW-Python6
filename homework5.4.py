x = int(input('x='))
y = int(input('y='))
i = 0
while i < x:
    j = 1
    while j < y:
        j += 1
        print('*', end='')
    print()
    i += 1