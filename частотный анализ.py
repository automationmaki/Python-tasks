from collections import defaultdict

text = open('input.txt', 'r', encoding='utf8')
words = defaultdict(int)
for line in text:
    for word in line.strip().split():
        words[word] += 1

frequency = defaultdict(list)
for word, freq in words.items():
    frequency[freq].append(word)
for freq, words in sorted(frequency.items(), key=lambda x: x[0], reverse=True):
    for word in sorted(words):
        print(word)
