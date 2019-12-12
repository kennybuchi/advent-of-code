from intCode import intCode
from itertools import permutations
inputFile = open('./2019/day7input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr))

#PART 1

iters = list(permutations(range(0, 5)))
maxOut = 0

for it in iters:
    output = 0
    for i in it:
        output = intCode(nums.copy(), [i, output])[0][0]
    if output > maxOut:
        maxOut = output

print('PART 1: ', maxOut)

#PART 2

nums = list(map(int, inputArr))

iters = list(permutations(range(5, 10)))
maxOut = 0

output = [0]

for it in iters:
    numArr = [nums.copy()] * 5
    iArr = [0] * 5
    outNum = 0
    j = 0
    while output != ['HALT']:
        outputTuple = intCode(numArr[j], [it[j], output[0]], iArr[j])
        outNum = output[0]
        output = outputTuple[0]
        iArr[j] = outputTuple[1]
        j = (j + 1) % 5

    if outNum > maxOut:
        maxOut = outNum

print('PART 2: ', maxOut)
