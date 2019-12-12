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

iters = list(permutations(range(5, 10)))
maxOut = 0

output = 0

for it in iters:
    num1 = nums.copy()
    num2 = nums.copy()
    num3 = nums.copy()
    num4 = nums.copy()
    num5 = nums.copy()
    numArr = [num1, num2, num3, num4, num5]
    iArr = [0] * 5
    inputArr = [[i] for i in it]
    inputArr[0] += [0]
    outNum = 0
    j = 0
    while 'HALT' not in inputArr[0]:
        output = intCode(numArr[j], inputArr[j], iArr[j])
        inputArr[(j + 1) % 5] += output[0]
        iArr[j] = output[1]
        j = (j + 1) % 5

    if inputArr[0][0] > maxOut:
        maxOut = inputArr[0][0]

print('PART 2: ', maxOut)
