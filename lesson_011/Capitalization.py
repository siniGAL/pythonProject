s=(str(input('Введите слов: ')))
s=s.lower()
s0=s[0].upper()
s=s.replace(s[0],s0,1)
print(s)