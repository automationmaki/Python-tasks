def sum(summary=0):
    num = -1
    try:
        num = int(input())
    except ValueError as err:
        print(err)
        print('Enter the number')
    else:
        summary += num
    if num != 0:
        return sum(summary)
    return summary


print(sum())
