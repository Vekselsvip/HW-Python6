y = int(input('print year'))
if y % 4 != 0:
    print('odd')
elif y % 100 == 0:
    if y % 400 == 0 :
        print('even')
    else:
        print('odd')
else:
    print('even')