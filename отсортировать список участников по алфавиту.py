open_data = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
data = open_data.read().split()
n = 0
result = {}
for i in data:
    if n % 4 == 0:
        result[data[n]] = (data[n + 1], data[n + 3])
    n += 1
for j in sorted(result.keys()):
    print(' '.join(map(str, (j, ' '.join(map(str, result[j]))))), file=outFile)
