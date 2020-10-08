s=(str(input('Введите слов: ')))
s_r=s[1:-1]
s_r=s_r.replace('','*')
s=s.replace(s[1:-1],s_r)
print(s)
