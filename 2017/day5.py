inputFile = open('/home/klee/aoc/2017/day5input.txt', 'r')
input = inputFile.read()

#DAY 1

def nextIndex(instructionList, index, length):
    newIndex = instructionList[index] + index
    if newIndex < 0 or newIndex >= length:
        return -1
    else:
        instructionList[index] += 1
        return newIndex

inputList = input.splitlines()
instructionList = list(map(int, inputList))
listLength = len(instructionList)
count = 0
index = 0

while index != -1:
    index = nextIndex(instructionList, index, listLength)
    count += 1

print(count)

#DAY 2

def nextIndexPart2(instructionList, index, length):
    newIndex = instructionList[index] + index
    if newIndex < 0 or newIndex >= length:
        return -1
    else:
        if instructionList[index] >= 3:
            instructionList[index] -= 1
        else:
            instructionList[index] += 1
        return newIndex

inputList = input.splitlines()
instructionList = list(map(int, inputList))
listLength = len(instructionList)
count = 0
index = 0

while index != -1:
    index = nextIndexPart2(instructionList, index, listLength)
    count += 1

print(count)