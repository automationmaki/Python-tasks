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
        m1 = numpy.array(self.matrix)
        return Matrix(m1 * other)

    def __rmul__(self, other):
        m2 = numpy.array(self.matrix)
        return Matrix(other * m2)


exec(stdin.read())
