from intCode import intCode
import time

inputFile = open('./2019/day13input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr)) + [0]*10000

#PART 1
arr = intCode(nums)[0]
count = 0
for i in range (2, len(arr) + 1, 3):
    if arr[i] == 2:
        count += 1

print('PART 1: ', count)

#PART 2

nums = list(map(int, inputArr)) + [0]*10000
intI = 0
relIndex = 0
nums[0] = 2
inp = [0]
score = 0
gameend = False
loops = 0

ball, paddle = -1, -1
start = time.time()

while True:

    output = intCode(nums, inp)
    arr = output[0]
    intI = output[1]
    relIndex = output[2]
    curBlocks = 0
    aa, bb = 0, 0

    for i in range (2, len(arr) + 1, 3):
        if arr[i-2] == -1 and arr[i-1] == 0:
            score = arr[i]
        if arr[i] == 2:
            curBlocks += 1
        if arr[i] == 4:
            ball = arr[i-2]
            aa, bb = arr[i-2], arr[i-1]
        if arr[i] == 3:
            paddle = arr[i-2]

    if time.time() - start > 5:
        print(curBlocks)
        start = time.time()

    if curBlocks == 0:
        break

    if paddle < ball:
        inp = [1]
    elif paddle > ball:
        inp = [-1]
    else:
        inp = [0]
print('PART 2: ', score)