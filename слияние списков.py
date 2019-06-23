lista = list(map(int, input().split()))
listb = list(map(int, input().split()))


def merge(a: list, b: list):

    lena = len(a)
    lenb = len(b)

    # если первый список длинее, то меняем
    # списки и переменные местами:
    if len(a) > lenb:
        a, b = b, a
        lena, lenb = lenb, lena

    i = 0   # индекс меньшего списка
    j = 0   # индекс большего списка
    listn = []   # новый список

    # цикл проходит только по меньшему списку:
    while i <= lena:

        # если конец одного из списка, то
        # добавляем оставшееся содержимое второго
        # списка в конец нового и выходим:
        if i == lena:
            listn = listn + b[j:lenb]
            return listn
        elif j == lenb:
            listn = listn + a[i:lena]
            return listn

        # проверяем числа списков и когда
        # берем число одного из списка в новый,
        # то увеличиваем соответствующий индекс:
        if a[i] < b[j]:
            listn.append(a[i])
            i += 1
        elif a[i] == b[j]:
            listn.append(a[i])
            listn.append(b[j])
            i += 1
            j += 1
        else:
            listn.append(b[j])
            j += 1


print(*merge(lista, listb))
