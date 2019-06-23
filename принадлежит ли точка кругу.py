def IsPointInCircle(x, y, xc, yc, r):
    return (x-xc)*(x-xc)+(y-yc)*(y-yc) <= r*r

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
