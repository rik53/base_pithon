"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, number):
        self.number = number.split('-')

    def number(self):
        try:
            digit = [int(i) for i in self.number]
            print(f'{digit[0]} - {digit[1]} - {digit[2]}')
        except Exception as err:
            print(f'Введите данные цифрами, {err}')

    @staticmethod
    def valid(val):
        el = val.split('-')
        if int(el[0]) not in range(1, 31):
            print('Введите верное число')
        elif int(el[1]) not in range(1, 13):
            print('Введите верный месяц')


forma = input('Введите дату в виде строки формата «день-месяц-год»: ')
date = Date(forma)
number = Date.number(date)
valid = Date.valid(forma)

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в 
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
n = int(input('Введите делимое: '))
m = int(input('Введите делитель: '))
class NewException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]
def division(a, b):
    if not b:
        raise NewException('Делить на 0 нельзя!!')
    return a /b
try:
    division(n, m)
except Exception as err:
    print(type(err), err)
print(n / m)

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на 
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать 
у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных 
элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь 
сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, 
сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и 
вносить его в список, только если введено число. Класс-исключение должен не позволить 
пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа 
скрипта не должна завершаться.
"""

class Exept:
    line = list()
    def __init__(self, number):
        self.number = number
    def addition(self):
        Exept.line.append(n)
    @staticmethod
    def error(er):
        try:
            cond = int(er)
        except ValueError:
            Exept.line.pop()
n = None
while n != 'stop':
    n = input('Введите число или напишите stop: ')
    exept = Exept(n)
    addition = Exept.addition(exept)
    exept_error = Exept.error(n)
else:
    print(Exept.line)

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также 
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы 
оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для 
приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа 
оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники 
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании 
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую 
структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем 
данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать 
строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум 
возможностей, изученных на уроках по ООП.
"""


class Warehouse:
    section = 5
    shelves = 20
    spots = 2500
    print(f'Максимальная загрузка склада {section} секций, {shelves} полок, {spots} мест')


class Equipment(Warehouse):
    count = Warehouse.spots
    subjects = {}

    def __init__(self, type, name, quantity, branch):
        self.branch = branch
        self.type = type
        self.name = name
        self.quantity = quantity
        Equipment.count -= self.quantity
        Equipment.subjects.update({self.type: [self.name, self.quantity, self.branch]})

    def __str__(self):
        return f'Добавили {self.name} Осталось свободных мест: {Equipment.count} '


class Printer(Equipment):
    cnt = 0

    def __init__(self, name, quantity, color):
        self.name = name
        self.quantity = quantity
        self.color = color
        Printer.cnt += self.quantity

    def __str__(self):
        return f'Вы добавили {self.name}, {self.color} принтер, Всего: {Printer.cnt} принтеров'


class Scanner(Equipment):
    cnt = 0

    def __init__(self, name, quantity, type_scaner):
        self.name = name
        self.quantity = quantity
        self.type_scaner = type_scaner
        Scanner.cnt += self.quantity

    def __str__(self):
        return f'Вы добавили {self.name}, {self.type_scaner} сканер, Всего: {Scanner.cnt} сканеров'


class Computer(Equipment):
    cnt = 0

    def __init__(self, name, quantity, kind):
        self.name = name
        self.quantity = quantity
        self.kind = kind
        Computer.cnt += self.quantity

    def __str__(self):
        return f'Вы добавили {self.name}, {self.kind} компьютер, Всего: {Computer.cnt} компьютеров'


cont = None
while cont != 'stop':
    tech = input('Введите наименование оргтехники (printer, scanner, computer) : ')
    if tech == 'printer':
        mark = input('Введите марку принтера: ')
        bran = input('Введите департамент или подразделение: ')
        try:
            qua = int(input('Введите колличество : '))
        except Exception as err:
            print(f'Введите число, {err}')
            continue
        var = input('Принтер цветной или черно-белый?: ')
        if var == 'цветной' or var == 'черно-белый':
            equipment = Equipment(tech, mark, qua, bran)
            printer = Printer(mark, qua, var)
            print(equipment)
            print(printer)
            cont = input('Для продолжения нажмите enter для окончания напишите stop: ')
        else:
            print('Выберете значение принтера: цветной или черно-белый')
            continue
    elif tech == 'scanner':
        mark = input('Введите марку сканера: ')
        bran = input('Введите департамент или подразделение: ')
        try:
            qua = int(input('Введите колличество : '))
        except Exception as err:
            print(f'Введите число, {err}')
            continue
        var = input('Сканер 3d или планшетный?: ')
        if var == '3d' or var == 'планшетный':
            equipment = Equipment(tech, mark, qua, bran)
            scanner = Scanner(mark, qua, var)
            print(equipment)
            print(scanner)
            cont = input('Для продолжения нажмите enter для окончания напишите stop: ')
        else:
            print('Выберете значение принтера: цветной или черно-белый')
        continue
    elif tech == 'computer':
        mark = input('Введите марку компьютера: ')
        bran = input('Введите департамент или подразделение: ')
        try:
            qua = int(input('Введите колличество : '))
        except Exception as err:
            print(f'Введите число, {err}')
            continue
        var = input('Компьютер стационарный или планшет?: ')
        if var == 'стационарный' or var == 'планшет':
            equipment = Equipment(tech, mark, qua, bran)
            computer = Computer(mark, qua, var)
            print(equipment)
            print(computer)
            cont = input('Для продолжения нажмите enter для окончания напишите stop: ')
        else:
            print('Выберете значение компьютера: стационарный или планшет')
        continue
print(Equipment.subjects)

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных 
экземпляров. Проверьте корректность полученного результата.
"""
class Complex_numbers:
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2
    def __str__(self):
        return f'{self.z1} + {self.z2}i'
    def __add__(self, other):
        z1 = self.z1 + other.z1
        z2 = self.z2 + other.z2
        return Complex_numbers(z1, z2)


complex_numbers = Complex_numbers(5, 7)
complex_numbers_2 = Complex_numbers(10, 3)
sum_complex_numbers = complex_numbers + complex_numbers_2
print(sum_complex_numbers)