p = [(172, 'Vasya'), (180, 'Petya'), (172, 'Fedya')]
def makeTuple(man):
    return(-man[0], man[1])
p.sort(key=makeTuple)
print(*p)
