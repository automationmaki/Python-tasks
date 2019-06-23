class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im


a = Complex()
b = Complex(1)
c = Complex(2, 3)
print(b.re, b.im)
print(c.re, c.im)

