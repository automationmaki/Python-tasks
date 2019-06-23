S, N = map(int, input().split())
volume = sorted([int(input()) for _ in range(N)])
amount = sum(volume)
while amount > S and N:
    amount -= volume.pop()
    N -= 1
print(N)
