a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2  # полупериметр
s = (p * (p - a) * (p - b) * (p - c))
if s < 0:
    s *= -1
print('{:.6f}'.format(pow(s, 0.5)))
