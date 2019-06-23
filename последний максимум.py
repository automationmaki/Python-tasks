a = list(map(int, input().split()))
index = 0
value = a[0]
for ind, val in enumerate(a):
    if val > value or val == value:
        index, value = ind, val
print(value, index)
