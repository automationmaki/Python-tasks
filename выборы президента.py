import io

candidates = {}
voices = 0

with io.open("input.txt", "r", encoding="utf-8") as inf:
    for name in map(str.strip, inf):
        candidates[name] = candidates.get(name, 0) + 1
        voices += 1


candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

with io.open("output.txt", "w", encoding="utf-8") as out:
    percent = candidates[0][1] / voices * 100
    if percent > 50:
        print(candidates[0][0], file=out)
    else:
        for name, _ in candidates[:2]:
            print(name, file=out)
out.close()
inf.close()
