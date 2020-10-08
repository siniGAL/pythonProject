s=str(input('Введите слово: '))


if s.find('h') < s.find('e') < s.find('l') < s.find('l',s.find('l')+1) < s.find('o'):
    print('YES')
else:
    print('NO')