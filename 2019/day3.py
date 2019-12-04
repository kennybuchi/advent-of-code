inputFile = open('./2019/day3input.txt', 'r')
input = inputFile.read()

#PART 1

def getClosest(x, y, curClosest):
    newDist = abs(x) + abs(y)
    return (newDist if newDist < curClosest else curClosest)

inputLines = input.splitlines()
firstWire = inputLines[0].split(',')
secondWire = inputLines[1].split(',')

change = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}

index = [0, 0]
visited = set()

for inst in firstWire:
    for i in range(int(inst[1:])):
        index = [x + y for x, y in zip(index, change[inst[0]])]
        visited.add(tuple(index))

closest = 9999999

index = [0, 0]

for inst in secondWire:
    for i in range(int(inst[1:])):
        index = [x + y for x, y in zip(index, change[inst[0]])]
        if tuple(index) in visited:
            closest = getClosest(index[0], index[1], closest)

print("PART 1: ", closest)

#PART 2

def getClosestSteps(steps1, steps2, curClosestSteps):
    newSteps = steps1 + steps2
    return (newSteps if newSteps < curClosestSteps else curClosestSteps)

change = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}

index = [0, 0]
visitedSteps = dict()
steps = 0

for inst in firstWire:
    for i in range(int(inst[1:])):
        steps += 1
        index = [x + y for x, y in zip(index, change[inst[0]])]
        indexTuple = tuple(index)
        if indexTuple not in visitedSteps:
            visitedSteps[indexTuple] = steps

closestSteps = 9999999

index = [0, 0]
steps = 0

for inst in secondWire:
    for i in range(int(inst[1:])):
        steps += 1
        index = [x + y for x, y in zip(index, change[inst[0]])]
        indexTuple = tuple(index)
        if indexTuple in visitedSteps:
            closestSteps = getClosestSteps(steps, visitedSteps[indexTuple], closestSteps)

print("PART 2: ", closestSteps)