a = float(input())
b = float(input())
c = float(input())
a != 0
di = b ** 2 - 4 * a * c
if di > 0:
    x1 = (-b - di ** (1/2)) / (2 * a)
    x2 = (-b + di ** (1/2)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    elif x1 > x2:
        print(x2, x1)
elif di == 0:
    x1 = (-b - di ** (1 / 2)) / (2 * a)
    print(x1)
else:
    print(" ")
