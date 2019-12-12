import numpy
from intCode import intCode

inputFile = open('./2019/day11input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr)) + [0]*10000

#PART 1

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
dirIndex = 0
painted = {}
blackOrWhite = 0
coords = [0, 0]

i = 0
relativeIndex = 0

while True:
    coordTuple = tuple(coords)
    blackOrWhite = painted[coordTuple] if coordTuple in painted else 0

    output = intCode(nums, [blackOrWhite], i, relativeIndex)
    i = output[1]
    relativeIndex = output[2]

    if output[0] == ['HALT']:
        break

    painted[coordTuple] = output[0][0]

    if output[0][1] == 0:
        dirIndex -= 1
    else:
        dirIndex += 1
    dirIndex %= 4
    coords[0] += directions[dirIndex][0]
    coords[1] += directions[dirIndex][1]

print("PART 1: ", len(painted))

#PART 2

nums = list(map(int, inputArr)) + [0]*10000

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
dirIndex = 0
painted = {(0, 0): 1}
blackOrWhite = 0
coords = [0, 0]

i = 0
relativeIndex = 0

while True:
    coordTuple = tuple(coords)
    blackOrWhite = painted[coordTuple] if coordTuple in painted else 0

    output = intCode(nums, [blackOrWhite], i, relativeIndex)
    i = output[1]
    relativeIndex = output[2]

    if output[0] == ['HALT']:
        break

    painted[coordTuple] = output[0][0]

    if output[0][1] == 0:
        dirIndex -= 1
    else:
        dirIndex += 1
    dirIndex %= 4
    coords[0] += directions[dirIndex][0]
    coords[1] += directions[dirIndex][1]


min_x = min([x[0] for x in painted.keys()])
max_x = max([x[0] for x in painted.keys()])
min_y = min([x[1] for x in painted.keys()])
max_y = max([x[1] for x in painted.keys()])

for y in range(max_y, min_y - 1, -1):
    for x in range(min_x, max_x + 1):
        if painted.get((x, y), 0) == 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()
