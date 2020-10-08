a,b,c=map(int,input("Введите три числа 1:10: ").split())

print(max(a+b+c, a*b*c, (a+b)*c, a*(b+c), a+b*c, a*b+c))
