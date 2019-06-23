def CountSort(a):
    counts = [0] * 101
    for i in a:
        counts[i] += 1
    a = []
    for i in range(101):
        a += [i] * counts[i]
    return a


a = list(map(int, input().split()))
print(*CountSort(a))
