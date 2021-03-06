"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
data = input('Введите построчно данные, Об окончании ввода данных свидетельствует пустая строка: ')
with open("my_file.txt", "w") as f_obj:
    print(data, file=f_obj)
while data != "":
    data = input('Введите построчно данные, Об окончании ввода данных свидетельствует пустая строка: ')
    with open("my_file.txt", "a") as f_obj:
        print(data, file=f_obj)

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("my_file.txt", "r") as obj:
    content2 = obj.readlines()
    print('Кол-во строк: ', len(content2))

with open("my_file.txt", "r") as f_obj:

    for line in f_obj:
        print('Кол-во слов в строке: ', len(line.split()))

"""
3. Создать текстовый файл (не программно), построчно записать фамилии 
сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

name = list()
sallary = list()
with open("my_file.txt", 'r') as obj:
    content = (obj.read()).split(',')
count = 0
for el in content:
    if count % 2 == 0:
        name.append(el)
    else:
        sallary.append(int(el))
    count += 1
cnt = 0
for i in sallary:
    if int(i) < 20000:
        print('Меньше 20000 получают: ', name[cnt],i)
    cnt += 1
print('Средняя величина дохода сотрудников', int((sum(sallary) / len(sallary))), 'руб.')

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен 
записываться в новый текстовый файл.
"""

word = list()
number = list()
rus_word = ['- Один \n', '- Два \n', '- Три \n', '- Четыре \n']
with open("my_file.txt", 'r') as obj:
    content = (obj.read()).split('\n')
for el in content:
    i = el.split('—')
    number.append(i[1])
count = 0
for elem in rus_word:
    word.append(number[count])
    word.append(elem)
count += 1
print(word)
with open("test.txt", 'w') as f_obj:
    content_new = f_obj.writelines(word)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

num = '1 2 3 4 5'
num_new = []
with open('my_file.txt', 'w') as obj:
    content = obj.write(num)
num = list(num.split())
for el in num:
    el = num_new.append(int(el))
print(sum(num_new))

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, 
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subjects = {}
with open('my_file.txt', 'r') as obj:
    lines = obj.readlines()
for el in lines:
    data = el.replace('(', ' ').split()
    subjects[data[0][:-1]] = sum(
        int(i) for i in data if i.isdigit()
    )
print(subjects)

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь 
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
subjects = {}
avr_prof = {}
prof = []
with open('my_file.txt', 'r') as obj:
    content = obj.readlines()
cnt = 0
for el in content:
    lin = el.split()
    subjects[lin[0]] = int(lin[2]) - int(lin[3])
    prof.append(int(lin[2]) - int(lin[3]))
avr_prof['average profit'] = int(sum(prof) / len(content))
res = [subjects, avr_prof]
with open('json_file.json', 'w') as json_obj:
    json.dump(res, json_obj)