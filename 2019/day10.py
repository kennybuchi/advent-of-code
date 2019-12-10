import math

inputFile = open('./2019/day10input.txt', 'r')
inputText = inputFile.read()

inputLines = inputText.splitlines()

x_len, y_len = len(inputLines[0]), len(inputLines)

asteroids = []

#PART 1

for i in range(y_len):
    for j in range(x_len):
        if inputLines[i][j] == '#':
            asteroids.append(tuple((j, i)))

def getAngle(x1, y1, x2, y2):
    return math.degrees(math.atan2( (y2 - y1), (x2 - x1))) % 360

maxCount = 0
asteroid = (0, 0)

for main in asteroids:
    vision = set()
    for secondary in asteroids:
        if main != secondary:
            vision.add(getAngle( main[0], main[1], secondary[0], secondary[1] ))
    if len(vision) > maxCount:
        maxCount = len(vision)
        asteroid = main

print('PART 1: ', maxCount)

#PART 2

bettingNum = 200

def getDistance(x1, y1, x2, y2):
    return math.sqrt( ( abs(x2 - x1) ** 2) + ( abs(y2 - y1) ** 2) )

order = {}

for secondary in asteroids:
    if asteroid != secondary:
        angle = (getAngle( asteroid[0], asteroid[1], secondary[0], secondary[1]) + 90) % 360
        distance = getDistance( asteroid[0], asteroid[1], secondary[0], secondary[1])
        ast_tuple = (distance, secondary)
        if angle not in order:
            order[angle] = []
        order[angle].append(ast_tuple)

def getKey(item):
    return item[0]

for k, v in order.items():
    order[k] = sorted(v, key=getKey)

count = 0
keys = sorted(order.keys())
newAst = (0, 0)

while count != bettingNum:
    for i in keys:
        if len(order[i]) > 0:
            j = order[i].pop(0)
            count += 1
            if count == 1 or count == 2 or count == 3 or count == 10 or count == 20:
                print(j[1]) 
            if count == bettingNum:
                newAst = j[1]
                break

print('PART 2: ', (newAst[0] * 100) + newAst[1])