x = int(input('print number '))
if x < 0:
    print(x)

x = int(input('print number '))
if x < 20:
    print('yes, it\'s less then 20')
else:
    print('it\'s at less 20')

x = int(input('print number '))
x = x % 2
if x == 0:
    print('it\'s even number')
else:
    print('it\'s odd number')

x, y, z = int(input('x=')), int(input('y=')), int(input('z='))
print(max(x, y, z))