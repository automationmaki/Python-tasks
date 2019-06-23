class ComplexError(BaseException):
    def __init__(self, complex, other):
        self.first = complex
        self.second = other
class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i'
    def __add__(self, other):
        result = Complex(self.re + other.re, self.im + other.im)
        return result
    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + other.re * self.im
        elif isinstance(other, int) or isinstance(other, float):
            re = self.re * other
            im = self.im * other
        else:
            error = ComplexError(self, other)
            raise error
        return Complex(re, im)
    __rmul__ = __mul__
class Point(Complex):
    def length(self):
        return (self.re ** 2 + self.im**2)**0.5
    def __str__(self):
        return str((self.re, self.im))


p1 = Complex(1, 1)
print(p1)