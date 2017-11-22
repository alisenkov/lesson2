d = {"x": 1, "y": 2, "z": 3}
k = d.keys()    # Список ключей
k.sort()        # Сортируем список ключей
 
for key in k:
    print "(%s => %s)" % (key, d[key])