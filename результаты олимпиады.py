num = int(input())
members = [input().split() for _ in range(num)]
for i in sorted(members, key=lambda x: int(x[1]), reverse=True):
    print(i[0])
