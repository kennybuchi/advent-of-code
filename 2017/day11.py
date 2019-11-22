inputFile = open('./2017/day11input.txt', 'r')
input = inputFile.read()

#PART 1

stepList = input.split(',')
steps = 0

x, y = 0, 0

for step in stepList:
    if step == 'nw':
        x -= 1
        y += 1
    elif step == 'n':
        y += 2
    elif step == 'ne':
        x += 1
        y += 1
    elif step == 'sw':
        x -= 1
        y -= 1
    elif step == 's':
        y -= 2
    elif step == 'se':
        x += 1
        y -= 1

abs_x = abs(x)
abs_y = abs(y)

while abs_x > 0 and abs_y > 0:
    abs_y -= 1
    abs_x -= 1
    steps += 1

steps += abs_x
steps += int(abs_y / 2)

print(steps)

#PART 2

furthest = 0

x, y = 0, 0

for step in stepList:
    if step == 'nw':
        x -= 1
        y += 1
    elif step == 'n':
        y += 2
    elif step == 'ne':
        x += 1
        y += 1
    elif step == 'sw':
        x -= 1
        y -= 1
    elif step == 's':
        y -= 2
    elif step == 'se':
        x += 1
        y -= 1

    abs_x = abs(x)
    abs_y = abs(y)

    steps = 0

    while abs_x > 0 and abs_y > 0:
        abs_y -= 1
        abs_x -= 1
        steps += 1

    steps += abs_x
    steps += int(abs_y / 2)

    if steps > furthest:
        furthest = steps

print(furthest)