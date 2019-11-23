import re

inputFile = open('./2017/day12input.txt', 'r')
input = inputFile.read()

#PART 1

programID = '0'
inputLines = input.splitlines()

connectionDict = dict()

for line in inputLines:
    vals = re.sub(r'[^0-9 ]', '', line).split()
    connectionDict[vals[0]] = []
    for i in range (1, len(vals)):
        connectionDict[vals[0]].append(vals[i])

toVisit = [programID]
visited = set(programID)

while len(toVisit) > 0:
    node = toVisit.pop(0)
    if node in connectionDict:
        for child in connectionDict[node]:
            if child not in visited:
                toVisit.append(child)
                visited.add(child)

print(len(visited))

#PART 2

inputLines = input.splitlines()

connectionDict = dict()
nodeSet = set()

for line in inputLines:
    vals = re.sub(r'[^0-9 ]', '', line).split()
    connectionDict[vals[0]] = []
    nodeSet.add(vals[0])
    for i in range (1, len(vals)):
        connectionDict[vals[0]].append(vals[i])

numGroups = 0
abc = 0

visited = set()

while len(nodeSet) > 0:
    curNode = nodeSet.pop()
    numGroups += 1
    toVisit = [curNode]

    visited.clear()
    visited.add(curNode)

    while len(toVisit) > 0:
        node = toVisit.pop(0)
        if node in connectionDict:
            for child in connectionDict[node]:
                if child not in visited:
                    toVisit.append(child)
                    visited.add(child)
                    if child in nodeSet:
                        nodeSet.remove(child)

print(numGroups)