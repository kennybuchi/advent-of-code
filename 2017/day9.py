inputFile = open('./2017/day9input.txt', 'r')
input = inputFile.read()

#PART 1

skipNext = False
isGarbage = False
level = 0
score = 0

for char in input:

    if isGarbage:
        #Skip anything after '!' char
        if skipNext:
            skipNext = False
            continue

        if char == '>':
            isGarbage = False
            continue

        elif char == '!':
            skipNext = True
            continue
    
    else:
        if char == '<':
            isGarbage = True
            continue
        
        elif char == '{':
            level += 1
            continue

        elif char == '}':
            if level > 0:
                score += level
                level -= 1
            continue

print(score)

#PART 2

skipNext = False
isGarbage = False
garbageCount = 0

for char in input:

    if isGarbage:
        #Skip anything after '!' char
        if skipNext:
            skipNext = False
            continue

        if char == '>':
            isGarbage = False
            continue

        elif char == '!':
            skipNext = True
            continue

        else:
            garbageCount += 1
            continue
    
    else:
        if char == '<':
            isGarbage = True
            continue

print(garbageCount)