s=str(input("Введите строку: "))

s=s.lower()
s=s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('y','')
s_r=s[0:-1]
s_r=s_r.replace('','.')
s=s.replace(s[0:-1],s_r)
print(s)
