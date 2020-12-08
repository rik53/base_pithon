income = int(input('Выручка, руб.: '))
cost = int(input('Издержки, руб.: '))
if income > cost:
    print('Прибыль')
    profit_cost = (income - cost) / income
    print('Рентабельность выручки: {:.2f} руб.'.format(profit_cost))
    empl = int(input('Количество сотрудников: '))
    profit_empl = (income - cost) / empl
    print('Прибыль фирмы в расчёте на одного сотрудника: {:.2f} руб.'.format(profit_empl))
elif income == cost:
    print('Компания работает в ноль')
else:
    print('Убыток')


