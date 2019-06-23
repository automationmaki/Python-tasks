from math import *
x = float(input())
if x - floor(x) < 0.5:
    x = floor(x)
else:
    x = ceil(x)
print(x)
