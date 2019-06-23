fin = open('input.txt')
myDict = {}
for line in fin:
    eng, latins = line.split('-')
    latinList = latins.split(',')
    eng = eng.strip()
    for latin in latinList:
        if latin.strip() not in myDict:
            myDict[latin.strip()] = []
        myDict[latin.strip()].append(eng)
print(myDict)
for latin in sorted(myDict):
    print(latin, '-', ', '.join(sorted(myDict[latin])))
