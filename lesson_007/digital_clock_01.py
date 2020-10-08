seconds=int(input("Введите колличество секунд: "))
print("Время на часах: %.2d:%.2d:%.2d" %((seconds//3600)%24, (seconds//60)%60, seconds%60))
