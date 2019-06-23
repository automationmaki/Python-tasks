i = list(input().split())
min = 1000
for k in range(len(i)):
    s = int(i[k])
    if (s < min)and(s > 0):
        min = s
print(min)
