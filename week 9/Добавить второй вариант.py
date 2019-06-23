from sys import stdin
from copy import deepcopy


class Matrix(object):
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.list2D]
            return matrix(result)
        elif self.dim_C != other.dim_R:
            return 'Нельзя перемножить матрицы таких размерностей'
        else:
            a = range(self.dim_C)
            b = range(self.dim_R)
            c = range(other.dim_C)
            result = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return matrix(result)


__rmul__ = __mul__


exec(stdin.read())
