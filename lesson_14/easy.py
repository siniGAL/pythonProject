n=str(input('Введите число опрошенных: '))
i=list(input('Введите результаты опроса: '))
if i.count('1') > 0:
    print('HARD')
else:
    print('EASY')