import re, math, json

inputFile = open('./2019/day14input.txt', 'r')
inputText = inputFile.read()
inputLines = inputText.splitlines()

#PART 1

def runReactions(numFuel, reactions):
    fuelDict = {'FUEL': numFuel}
    while True:
        dictState = json.dumps(fuelDict)
        keys = tuple(fuelDict.keys())
        for item in keys:
            if item == 'ORE':
                continue

            numReactions = math.ceil(fuelDict[item] / reactions[item][item])
            for mat in reactions[item]:
                if mat == item:
                    continue
                if mat in fuelDict:
                    fuelDict[mat] += reactions[item][mat] * numReactions
                else:
                    fuelDict[mat] = reactions[item][mat] * numReactions
                
            fuelDict[item] -= reactions[item][item] * numReactions
        if dictState == json.dumps(fuelDict):
            break
    keys = tuple(fuelDict.keys())
    for item in keys:
        if fuelDict[item] == 0:
            del fuelDict[item]
        elif fuelDict[item] < 0:
            fuelDict[item] = abs(fuelDict[item])
    return fuelDict['ORE']

reactions = {}
for line in inputLines:
    reg = re.sub(r'[^0-9 A-Z]', '', line).split()
    reaction = {}
    for i in range(0, len(reg) - 2, 2):
        reaction[reg[i+1]] = int(reg[i])
    reaction[reg[-1]] = int(reg[-2])
    reactions[reg[-1]] = reaction

oreForFuel = runReactions(1, reactions)
print('PART 1: ', oreForFuel)

#PART 2
oreOwned = 1000000000000

min, max = 0, math.ceil(oreOwned / oreForFuel) * 2

#This just guesses the answer in log(n) time
while min != max:
    avg = math.ceil((max - min) / 2) + min
    oreNeeded = runReactions(avg, reactions)
    if oreNeeded < oreOwned:
        min = avg
    elif oreNeeded == oreOwned:
        min, max = avg, avg
    else:
        max = avg

    if max - min == 1:
        max = min

print('PART 2: ', min)