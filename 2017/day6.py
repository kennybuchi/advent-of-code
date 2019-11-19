inputFile = open('/home/klee/aoc/2017/day6input.txt', 'r')
input = inputFile.read()

#PART 1

def findMaxIndex(numList):
    return numList.index(max(numList))

inputList = input.split()
numList = list(map(int, inputList))
numSet = set()
count = 0

while str(numList) not in numSet:
    numSet.add(str(numList))
    index = findMaxIndex(numList)
    maxVal = numList[index]
    numList[index] = 0
    for i in range(maxVal):
        index += 1
        if index >= len(numList):
            index = 0
        numList[index] += 1
    count += 1

print(count)

#PART 2

inputList = input.split()
numList = list(map(int, inputList))
numDict = dict()
count = 0

while str(numList) not in numDict:
    numDict[str(numList)] = count
    index = findMaxIndex(numList)
    maxVal = numList[index]
    numList[index] = 0
    for i in range(maxVal):
        index += 1
        if index >= len(numList):
            index = 0
        numList[index] += 1
    count += 1

loopSize = count - numDict[str(numList)]
print(loopSize)