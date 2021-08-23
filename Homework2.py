from math import ceil

x = int(input('number a flat '))
if x <= 36:
    x = ceil(x / 4)
    print(x, 'floor', '1 porch')
elif x <= 72:
    x = ceil((x - 36) / 4)
    print(x, 'floor', '2 porch')
elif x <= 108:
    x = ceil((x - 72) / 4)
    print(x, 'floor', '3 porch')
elif x <= 144:
    x = ceil((x - 108)/4)
    print(x, 'floor', '4 porch')
else:
    print('maybe anther number ?')