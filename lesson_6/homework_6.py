"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""
import time
class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        end = None
        new_color = []
        red = 'Красный'
        yellow = 'Желтый'
        green = 'Зеленый'
        while end != 'stop':
            print(red)
            time.sleep(7)
            new_color.append(red)
            print(yellow)
            time.sleep(2)
            new_color.append(yellow)
            print(green)
            time.sleep(7)
            new_color.append(green)
            if TrafficLight._color != new_color:
                print('Нарушение проверки порядка режимов')
                break
            end = input('Для прекращения работы светофора нажмите:stop ')
TrafficLight = TrafficLight()
TrafficLight.running()
"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого 
для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта 
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. 
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    __length = 0
    __width = 0
    def __init__(self, length, width, weight_per_1sm, think):
        self.weight_per_1sm = weight_per_1sm
        self.think = think
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна = {length * width * weight_per_1sm * think} т.')
user_length = int(input('Введите длину дороги в метрах: '))
user_width = int(input('Введите ширину дороги в метрах: '))
user_weight_per_1sm = int(input('Введите масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см в кг.: '))
user_think = int(input('Введите число см. толщины полотна: '))
Road(user_length, user_width, user_weight_per_1sm, user_think)

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, 
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться 
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы 
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров).
"""
user_name = input('Введите имя сотрудника:')
user_surname = input('Введите фамилию сотрудника:')
user_position = input('Введите должность сотрудника:')
try:
    user_wage = int(input('Введите оклад сотрудника:'))
    user_bonus = int(input('Введите премию сотрудника:'))
except ValueError as err:
    print(f'Введите число, {err}')
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus, )
    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'
    def get_total_income(self):
        return self.wage + self.bonus

pos = Position(user_name, user_surname, user_position, user_wage, user_bonus)
print(pos.get_full_name())
print(f'Должность: {pos.position}')
print('Доход с учетом премии:', pos.get_total_income())

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, 
name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: 
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
выведите результат. Выполните вызов методов и также покажите результат.
"""
class Car:
    show_speed = None
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        print(f'Вы выбрали себе {self.name} {self.color} цвета с максимальной скоростью {self.speed}. Это полицейская машина = {self.is_police}')
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('машина повернула')
class TownCar(Car):
    def __init__(self, show_speed):
        self.show_speed = show_speed
        print(f'Ваша скорость: {self.show_speed}')
        if self.show_speed > 60:
            print('Ваша максимальная скорость 60 км/ч')
class SportCar(Car):
    def __init__(self, show_speed):
        self.show_speed = show_speed
        print(f'Ваша скорость: {self.show_speed}')
class WorkCar(Car):
    def __init__(self, show_speed):
        self.show_speed = show_speed
        print(f'Ваша скорость: {self.show_speed}')
        if self.show_speed > 40:
            print('Ваша максимальная скорость 40 км/ч')
class PoliceCar(Car):
    def __init__(self, show_speed):
        self.show_speed = show_speed
        print(f'Ваша скорость: {self.show_speed}')
while True:
    cars = input('Выберете себе машину(TownCar, SportCar, WorkCar, PoliceCar) и запишите ее: ')
    if cars != 'TownCar' and cars != 'SportCar' and cars != 'WorkCar' and cars != 'PoliceCar':
        print('Выберите себе автомобиль из списка (TownCar, SportCar, WorkCar, PoliceCar)')
    else:
        break
if cars == 'TownCar':
    sp = 150
    col = 'Blue'
    nm = 'Kia'
    pl = 0
    TownCar(int(input('Введите значение вашей текущей скорости: ')))
elif cars == 'SportCar':
    sp = 250
    col = 'Red'
    nm = 'Ferrari'
    pl = 0
    SportCar(input('Введите значение вашей текущей скорости: '))
elif cars == 'WorkCar':
    sp = 80
    col = 'Black'
    nm = 'Opel'
    pl = 0
    WorkCar(int(input('Введите значение вашей текущей скорости: ')))
elif cars == 'PoliceCar':
    sp = 200
    col = 'Blue and White'
    nm = 'Ford'
    pl = 1
    PoliceCar(input('Введите значение вашей текущей скорости: '))
c = Car(sp, col, nm, pl) #+ show_speed
cmd = None
while cmd != 'end':
    cmd = input('Если вы хотите чтобы машина поехала напишите: go , остановилась: stop, повернула: turn, если вы приехали: end: ')
    if cmd == 'go':
        c.go()
    elif cmd == 'stop':
        c.stop()
    elif cmd == 'turn':
        c.turn()
    elif cmd == 'end':
        print('Вы уже приехали')

"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title 
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три 
дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать 
переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
    def __call__(self, *args, **kwargs):
        self.draw()
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки, ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки, карандашем')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки, маркером')

st = Stationery('paint')
st()
pen = Pen('pen')
pen()
pencil = Pencil('pencil')
pencil()
handle = Handle('handle')
handle()