a, b, c = int(input('a=')), int(input('b=')), int(input('c='))
if a + b > c:
    print('ok')
elif a + c > b:
    print('ok')
elif c + b > a:
    print('ok')
else:
    print('error')