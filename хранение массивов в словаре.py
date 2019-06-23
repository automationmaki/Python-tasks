gasCost = {}
n = int(input())
costs = list(map(int, input().split()))
btypes = (92, 95, 98)
for now in range(len(btypes)):
    gasCost[btypes[now]] = costs[now]
for i in range(n - 1):
    costs = list(map(int, input().split()))
    for now in range(len(btypes)):
        gasCost[btypes[now]] = min(costs[now], gasCost[btypes[now]])
print(gasCost[92], gasCost[95], gasCost[98])
