class Man:
    height = 0
    name = ''
p = []
n = int(input())
for i in range(n):
    h, n = input().split()
    h = int(h)
    man = Man()
    man.height = h
    man.name = n
    p.append(man)
def makeTuple(man):
    return (man.height, man.name)
p.sort(key=makeTuple)
for now in p:
    print(now.height, now.name)
