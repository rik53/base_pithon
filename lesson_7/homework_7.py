"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной
схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, mtx_x, mtx_y):
        self.mtx_x = mtx_x
        self.mtx_y = mtx_y

    def __str__(self):  # - метод возращает строку
        return f'{self.mtx_x}, {self.mtx_y}'

    def __add__(self, other):  # - метод суммы
        line = [(self.mtx_x)]
        line_2 = [(other.mtx_x)]
        line_3 = [(self.mtx_y)]
        line_4 = [(other.mtx_y)]

        x = []
        y = []

        for i in range(len(line)):
            for j in range(len(line[0])):

                x.append(line[i][j] + line_2[i][j])
                y.append(line_3[i][j] + line_4[i][j])

            return Matrix(x, y)
point_1 = Matrix([1, 2, 3], [7, 8, 9])
point_2 = Matrix([4, 5, 6], [10, 11, 12])
point3 = point_1 + point_2
print(point3)

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность 
(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом 
проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) 
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
 для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу 
декоратора @property.
"""

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def get_sq_full(self):
        return f'Общий расхода ткани: {((self.v / 6.5 + 0.5) + (2 * self.h + 0.3)):.2f} метров'
class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cons_coat(self):
        return f'Расход ткани на пальто: {((self.v / 6.5 + 0.5)):.2f} метров'
class Siut(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cons_siut(self):
        return f'Расход ткани на костюм: {((2 * self.h + 0.3)):.2f} метров'

coat = Coat(22)
print(coat.cons_coat)
siut = Siut(12)
print(siut.cons_siut)
clothes = Clothes(12, 22)
print(clothes.get_sq_full)

"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
 вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны 
 применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное 
 (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться 
 округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме 
ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества 
ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение 
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное 
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество 
ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно 
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
 все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод 
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() 
вернет строку: *****\n*****\n*****.
"""

class Cell:
    def __init__(self, q_cell):
        self.q_cell = q_cell
    def __str__(self):
        return f'{self.q_cell}'
    def __add__(self, other):
        x = self.q_cell + other.q_cell
        return Cell(x)
    def __sub__(self, other):
        x = self.q_cell - other.q_cell
        return Cell(x)
    def __mul__(self, other):
        x = self.q_cell * other.q_cell
        return Cell(x)
    def __truediv__(self, other):
        x = self.q_cell // other.q_cell
        return Cell(x)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.q_cell / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.q_cell % cells_in_row)}'
        return row



cell = Cell(10)
cell_2 = Cell(5)
cell_sum = cell + cell_2
cell_sub = cell - cell_2
cell_mul = cell * cell_2
cell_truediv = cell / cell_2
print(f'Сумма: {cell_sum}')
print(f'Вычитание: {cell_sub}')
print(f'Умножение: {cell_mul}')
print(f'Деление: {cell_truediv}')
print({cell.make_order(2)})