s = input()
gasCost = {}
n = int(input())
a92, a95, a98 = map(int(input().split()))
gasCost[92] = a92
gasCost[95] = a95
gasCost[98] = a98
for i in range(n - 1):
    a92, a95, a98 = map(int(input().split()))
    gasCost[92] = min(a92, gasCost[92])
    gasCost[95] = min(a95, gasCost[95])
    gasCost[98] = min(a98, gasCost[98])
print(gasCost[92], gasCost[95], gasCost[98])
