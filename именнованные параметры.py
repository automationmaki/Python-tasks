def printList(lst, mySep=' '):
    for i in range(len(lst) - 1):
        print(lst[i], mySep, sep='', end='')
    print(lst[-1], sep='')
printList([1, 2, 3], mySep='a')
printList([5, 6, 7]), 