fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
print(sum(map(int, fin.readlines())), file=fout)
fout.close()