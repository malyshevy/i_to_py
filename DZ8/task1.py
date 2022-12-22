'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''


class Matrix:
    def __init__(self, list_first):
        self.list_first = list_first

    def __str__(self):
        for j in self.list_first:
            for i in j:
                print(f"-{i}", end="")
            print()

    def __add__(self, list_second):
        for i in range(len(self.list_first)):
            for i_2 in range(len(list_second.list_first[i])):
                self.list_first[i][i_2] = self.list_first[i][i_2] + list_second.list_first[i][i_2]
        Matrix.__str__(self)


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_second = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix.__add__(matrix_second))
