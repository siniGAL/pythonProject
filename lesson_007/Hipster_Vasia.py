red, blue = map(int, input("Сколько носков у хипстера Васи? ").split())
print("Вася сможет ходить по моде %s дня(ей) и как обсос %s дня(ей)"%(min(red, blue), (max(red, blue)-min(red, blue))//2))
