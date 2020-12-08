sekonds = int(input('Введите время в секундах: '))
hours = sekonds // 3600
minuts = (sekonds - (hours * 3600)) // 60
sekonds = (sekonds - (hours * 3600) - minuts * 60)
print('%02d : %02d : %02d' % (hours, minuts, sekonds))
