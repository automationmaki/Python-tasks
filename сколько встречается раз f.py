s = input()
count = len(s) - len(s.replace('f', ''))
if count == 0:
    pass
elif count == 1:
    print(s.index('f'))
else:
    print(s.index('f'), s.rindex('f'))
