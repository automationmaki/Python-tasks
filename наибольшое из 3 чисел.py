x = int(input())
y = int(input())
a = int(input())
if x > a or y > a:
    if x > y:
        print(x)
    else:
        print(y)
else:
    print(a)
