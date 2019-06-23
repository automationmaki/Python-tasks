b = open("input.txt", "r", encoding="utf-8")
a = []
for i in b.read().split('\n'):
    a += i.split()
print(len(set(a)))
