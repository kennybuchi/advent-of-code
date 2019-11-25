import re

inputFile = open('./2017/day13input.txt', 'r')
input = inputFile.read()

#PART 1

inputList = input.splitlines()

depthRange = dict()
for line in inputList:
    vals = re.sub(r'[^0-9 ]', '', line).split()
    depthRange[int(vals[0])] = int(vals[1])

severity = 0

for depth, d_range in depthRange.items():
    loopLength = (d_range - 1) * 2
    if depth % loopLength == 0:
        severity += (depth * d_range)

print(severity)

#PART 2

START = time.time()

inputList = input.splitlines()

depthRange = dict()
maxRange = 0

for line in inputList:
    vals = re.sub(r'[^0-9 ]', '', line).split()
    depthRange[int(vals[0])] = int(vals[1])
    if int(vals[1]) > maxRange:
        maxRange = int(vals[1])

delay = 0
success = False

while not success:
    success = True

    for depth, d_range in depthRange.items():
        loopLength = (d_range - 1) * 2
        if (depth + delay) % loopLength == 0:
            success = False
            delay += 1
            break

print(delay)