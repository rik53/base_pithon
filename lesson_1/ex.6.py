a = int(input('Результат первого дня:'))
b = int(input('Желаемый результат: '))
day = 1
while a <= b:
    if a <= b:
        a += (a / 100) * 10
        day += 1
else:
    print(day)
