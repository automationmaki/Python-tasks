a = int(input())
b = int(input())


def summ(a, b):
    s = 0
    if a != 0:
        a -= 1
        s += 1
    if b != 0:
        b -= 1
        s += 1
    return 0 if s == 0 else s + summ(a, b)

print(summ(a, b))
