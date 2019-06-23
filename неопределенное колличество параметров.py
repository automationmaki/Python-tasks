def myMin(first, *others):
    nowMin = first
    for now in others:
        if now < nowMin:
            nowMin = now
    return nowMin


print(myMin(5, 2, 3, 4))
print(myMin(1))
