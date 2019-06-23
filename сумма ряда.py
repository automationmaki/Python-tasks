n = int(input())
seqSum = 0.0
i = 1
while i <= n:
    s = 1.0/(i**2)
    seqSum += s
    i = i + 1
print(seqSum)
