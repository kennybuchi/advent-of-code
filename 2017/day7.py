import re
import sys
inputFile = open('./2017/day7input.txt', 'r')
input = inputFile.read()

#PART 1
nameList = re.sub(r'[^a-z \n]', '', input).split()
nameCount = dict()

for name in nameList:
    if name not in nameCount:
        nameCount[name] = 1
    else:
        nameCount[name] += 1

bottomProgram = str()
for name in nameCount:
    if nameCount[name] == 1:
         bottomProgram = name
         break

print(bottomProgram)

#PART 2

class Node:
    def __init__(self, name, initWeight, weight):
        self.name = name
        self.initWeight = initWeight
        self.weight = weight

inputLines = input.splitlines()
nodeDict = dict()
toRemove = set()


for line in inputLines:
    vals = re.sub(r'[^a-z 0-9]', '', line).split()
    if len(vals) == 2:
        nodeDict[vals[0]] = Node(vals[0], int(vals[1]), int(vals[1]))
        toRemove.add(line)

for line in toRemove:
    inputLines.remove(line)

toRemove.clear()

while len(inputLines) >= 1:
    for line in inputLines:
        vals = re.sub(r'[^a-z 0-9]', '', line).split()
        initWeight = int(vals[1])
        weight = initWeight

        getWeight = True
        for i in range(2, len(vals)):
            if vals[i] not in nodeDict:
                getWeight = False
                break
        
        if getWeight:
            childSet = set()

            for i in range(2, len(vals)):
                weight += nodeDict[vals[i]].weight
                childSet.add(nodeDict[vals[i]].weight)
            
            if len(childSet) > 1:
                firstChildWeight = nodeDict[vals[2]].weight
                for i in range(3, len(vals)):
                    newWeight = 0
                    if nodeDict[vals[i]].weight > firstChildWeight:
                        if i > 3:
                            newWeight = nodeDict[vals[i]].initWeight - (nodeDict[vals[i]].weight - firstChildWeight)
                        else:
                            if firstChildWeight == nodeDict[vals[4]].weight:
                                newWeight = nodeDict[vals[i]].initWeight - (nodeDict[vals[i]].weight - firstChildWeight)
                            else:
                                newWeight = nodeDict[vals[2]].initWeight + (nodeDict[vals[3]].weight - nodeDict[vals[2]].weight)
                    elif nodeDict[vals[i]].weight < firstChildWeight:
                        if i > 3:
                            newWeight = nodeDict[vals[i]].initWeight + (firstChildWeight - nodeDict[vals[i]].weight)
                        else:
                            if firstChildWeight == nodeDict[vals[4]].weight:
                                newWeight = nodeDict[vals[i]].initWeight = (firstChildWeight - nodeDict[vals[i]].weight)
                            else:
                                newWeight = nodeDict[vals[2]].initWeight + (nodeDict[vals[2]].weight - nodeDict[vals[3]].weight)
                    print(newWeight)
                    sys.exit()
            
            
            nodeDict[vals[0]] = Node(vals[0], initWeight, weight)
            toRemove.add(line)
            
    for line in toRemove:
        inputLines.remove(line)
    
    toRemove.clear()

# nodeDict[vals[0]] = Node(vals[0], True, vals[1], vals[2:])