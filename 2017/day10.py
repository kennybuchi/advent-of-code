import sys
inputFile = open('./2017/day10input.txt', 'r')
input = inputFile.read()

listSize = 256

#PART 1

def twistList(list, listSize, index, length):
    endIndex = (index + length - 1) % listSize
    for i in range(index, (index + int(length/2))):
        list[index], list[endIndex] = list[endIndex], list[index]
        index += 1
        index = index % listSize
        endIndex -= 1

list = [i for i in range(listSize)]

lengthList = input.split(',')
index = 0
skip = 0

for lengthStr in lengthList:
    length = int(lengthStr)

    twistList(list, listSize, index, length)

    index += length
    index += skip
    skip += 1

    index = index % listSize
    
firstTwoMult = list[0] * list[1]
print(firstTwoMult)

#PART 2

list = [i for i in range(listSize)]

finalLengths = [17, 31, 73, 47, 23]
lengthList = [ord(char) for char in input]
lengthList.extend(finalLengths)

index = 0
skip = 0

for i in range(64):
    for length in lengthList:

        twistList(list, listSize, index, length)

        index += length
        index += skip
        skip += 1

        index = index % listSize

hashStr = ''

for i in range(16):
    start = i * 16
    xor = 0
    for j in range(16):
        xor ^= list[start + j]
    hashStr += format(xor, 'x').zfill(2)

print(hashStr)