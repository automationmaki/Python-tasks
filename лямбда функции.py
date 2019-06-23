points = [(1, 1), (5, 1), (10, 10)]
points.sort(key=lambda p: p[0]**2 + p[1]**2)
print(*points)
