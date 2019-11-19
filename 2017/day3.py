import sys
inputFile = open('./2017/day3input.txt', 'r')
input = inputFile.read()

#READ INPUT
inputNum = int(input)

#PART 1

if inputNum == 1:
    distance = 0

else:
    baseSqrt = 1
    while inputNum > baseSqrt ** 2:
        baseSqrt += 2

    outerBase = baseSqrt ** 2
    secondMostOuterBase = ( (baseSqrt - 2) ** 2 )

    adjustedInput = inputNum - secondMostOuterBase

    rightEdgeMiddle = int(baseSqrt/2 + 1)

    while adjustedInput - (baseSqrt - 1)  > 0:
        adjustedInput -= (baseSqrt - 1)

    distance = abs(rightEdgeMiddle - adjustedInput) + (int(baseSqrt / 2) + 1)

print(distance)

#PART 2

def getVal(arr, x, y):
    sum = 0
    for a in range(x-1,x+2):
        for b in range(y-1,y+2):
            sum += arr[a][b]
    if sum > inputNum:
        print(sum)
        sys.exit()
    return sum

baseSqrt = 1
while inputNum > baseSqrt ** 2:
    baseSqrt += 2

arr = [[0] * (baseSqrt) for i in range(baseSqrt)]

center = int((baseSqrt - 1) / 2)

x = center
y = center

arr[x][y] = 1

for i in range(3,baseSqrt,2):
    y += 1
    arr[x][y] = getVal(arr, x, y)
    for j in range(i-2):
        x += 1
        arr[x][y] = getVal(arr, x, y)
    for j in range(i-1):
        y -= 1
        arr[x][y] = getVal(arr, x, y)
    for j in range(i-1):
        x -= 1
        arr[x][y] = getVal(arr, x, y)
    for j in range(i-1):
        y += 1
        arr[x][y] = getVal(arr, x, y)