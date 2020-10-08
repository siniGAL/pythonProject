s=str(input('Введите слово:'))

if s.rfind('f',s.find('f')+1) > 0:
    print(s.find('f'), s.rfind('f',s.find('f')))
else:
    print(s.find('f'))