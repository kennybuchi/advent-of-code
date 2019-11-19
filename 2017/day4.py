from collections import Counter

inputFile = open('/home/klee/aoc/2017/day4input.txt', 'r')
input = inputFile.read()

#PART 1

numValidPhrases = 0
lines = input.splitlines()

for line in lines:
    words = line.split()
    wordCount = Counter(words)

    valid = True
    for word in words:
        if wordCount[word] > 1:
            valid = False
            break
    
    if valid:
        numValidPhrases += 1

print(numValidPhrases)

#PART 2
numValidPhrases = 0
lines = input.splitlines()

for line in lines:
    words = line.split()

    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))

    wordCount = Counter(words)

    valid = True
    for word in words:
        if wordCount[word] > 1:
            valid = False
            break
    
    if valid:
        numValidPhrases += 1

print(numValidPhrases)