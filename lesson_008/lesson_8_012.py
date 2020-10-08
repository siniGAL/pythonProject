a=int(input("Введите число: "))
b=int(input("Введите число: "))
c=int(input("Введите число: "))
a=a**2
b=b**2
c=c**2
print(a==b+c or b==c+a or c==a+b)