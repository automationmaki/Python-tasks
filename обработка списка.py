a = int(input())
b = list(map(int, input().split()))
c = int(input())
print(min(b, key=lambda a: abs(a - c)))
