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
        return Complex(re, im)
    __rmul__ = __mul__


a = Complex()
b = Complex(1, 1)
c = Complex(2, 3)
print(2 * b)
