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
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + other.re * self.im
        return Complex(re, im)


a = Complex()
b = Complex(1, 1)
c = Complex(2, 3)
print(b * c)
