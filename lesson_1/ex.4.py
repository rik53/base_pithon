number = int(input('Введите целое положительное число: '))
max = number % 10
number //= 10
while number >0:
    if number % 10 > max:
        max = number % 10
    number //= 10
print(max)
