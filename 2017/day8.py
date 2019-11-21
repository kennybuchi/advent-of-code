inputFile = open('./2017/day8input.txt', 'r')
input = inputFile.read()

#PART 1
inputLines = input.splitlines()

var = dict()

for line in inputLines:
    inputArr = line.split()

    #Add variables if they don't exist
    if inputArr[0] not in var:
        var[inputArr[0]] = 0
    
    if inputArr[4] not in var:
        var[inputArr[4]] = 0

    #Check conditional
    conditional = False

    if inputArr[5] == ">":
        conditional = var[inputArr[4]] > int(inputArr[6])
    elif inputArr[5] == "<":
        conditional = var[inputArr[4]] < int(inputArr[6])
    elif inputArr[5] == ">=":
        conditional = var[inputArr[4]] >= int(inputArr[6])
    elif inputArr[5] == "<=":
        conditional = var[inputArr[4]] <= int(inputArr[6])
    elif inputArr[5] == "==":
        conditional = var[inputArr[4]] == int(inputArr[6])
    elif inputArr[5] == "!=":
        conditional = var[inputArr[4]] != int(inputArr[6])

    if conditional:
        if inputArr[1] == "inc":
            var[inputArr[0]] += int(inputArr[2])
        elif inputArr[1] == "dec":
            var[inputArr[0]] -= int(inputArr[2])

maxVal = -999999999
for v in var:
    if var[v] > maxVal:
        maxVal = var[v]

print(maxVal)

#PART 2
inputLines = input.splitlines()

var = dict()
highestHeld = 0

for line in inputLines:
    inputArr = line.split()

    #Add variables if they don't exist
    if inputArr[0] not in var:
        var[inputArr[0]] = 0
    
    if inputArr[4] not in var:
        var[inputArr[4]] = 0

    #Check conditional
    conditional = False

    if inputArr[5] == ">":
        conditional = var[inputArr[4]] > int(inputArr[6])
    elif inputArr[5] == "<":
        conditional = var[inputArr[4]] < int(inputArr[6])
    elif inputArr[5] == ">=":
        conditional = var[inputArr[4]] >= int(inputArr[6])
    elif inputArr[5] == "<=":
        conditional = var[inputArr[4]] <= int(inputArr[6])
    elif inputArr[5] == "==":
        conditional = var[inputArr[4]] == int(inputArr[6])
    elif inputArr[5] == "!=":
        conditional = var[inputArr[4]] != int(inputArr[6])

    if conditional:
        if inputArr[1] == "inc":
            var[inputArr[0]] += int(inputArr[2])
            if var[inputArr[0]] > highestHeld:
                highestHeld = var[inputArr[0]]
        elif inputArr[1] == "dec":
            var[inputArr[0]] -= int(inputArr[2])


print(highestHeld)