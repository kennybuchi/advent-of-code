from intCode import intCode
import random

inputFile = open('./2019/day15input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr)) + [0]*10000

output = 0
distance = 0

command = 0
directions = { 1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0) }
location = [0, 0]
visited = {(0,0): 0}
stack = []
permChoices = (1, 2, 3, 4)
ic_i = 0
ic_offset = 0

def oppositeDir(dir):
    if dir == 1:
        return 2
    if dir == 2:
        return 1
    if dir == 3:
        return 4
    if dir == 4:
        return 3

while output != 2:
    choices = [1, 2, 3, 4]
    for choice in permChoices:
        choiceLoc = tuple([location[0] + directions[choice][0], location[1] + directions[choice][1]])
        if choiceLoc in visited and visited[choiceLoc] < distance + 2:
            choices.remove(choice)

    if len(choices) == 0:
        inputVal = oppositeDir(stack.pop())
        outputTuple = intCode(nums, [inputVal], ic_i, ic_offset)
        location[0] += directions[inputVal][0]
        location[1] += directions[inputVal][1]
        output = outputTuple[0][0]
        ic_i = outputTuple[1]
        ic_offset = outputTuple[2]
        distance -= 1
        continue

    inputVal = random.choice(choices)
    outputTuple = intCode(nums, [inputVal], ic_i, ic_offset)
    output = outputTuple[0][0]
    ic_i = outputTuple[1]
    ic_offset = outputTuple[2]

    if output == 0:
        visited[tuple([location[0] + directions[inputVal][0], location[1] + directions[inputVal][1]])] = -1
    elif output == 1:
        location[0] += directions[inputVal][0]
        location[1] += directions[inputVal][1]
        distance += 1
        visited[tuple(location)] = distance
        stack.append(inputVal)
    elif output == 2:
        distance += 1
        location[0] += directions[inputVal][0]
        location[1] += directions[inputVal][1]
        break

print('PART 1: ' + str(distance))

#PART 2

oxygenStart = location.copy()

nums = list(map(int, inputArr)) + [0]*10000

output = 0
distance = 0

command = 0
directions = { 1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0) }
location = oxygenStart.copy()
visited = {tuple(oxygenStart): 0}
stack = []
permChoices = (1, 2, 3, 4)
ic_i = 0
ic_offset = 0

while True:
    choices = [1, 2, 3, 4]
    for choice in permChoices:
        choiceLoc = tuple([location[0] + directions[choice][0], location[1] + directions[choice][1]])
        if choiceLoc in visited and visited[choiceLoc] < distance + 2:
            choices.remove(choice)

    if len(choices) == 0:
        if len(stack) == 0:
            break
        inputVal = oppositeDir(stack.pop())
        outputTuple = intCode(nums, [inputVal], ic_i, ic_offset)
        location[0] += directions[inputVal][0]
        location[1] += directions[inputVal][1]
        output = outputTuple[0][0]
        ic_i = outputTuple[1]
        ic_offset = outputTuple[2]
        distance -= 1
        continue

    inputVal = random.choice(choices)
    outputTuple = intCode(nums, [inputVal], ic_i, ic_offset)
    output = outputTuple[0][0]
    ic_i = outputTuple[1]
    ic_offset = outputTuple[2]

    if output == 0:
        visited[tuple([location[0] + directions[inputVal][0], location[1] + directions[inputVal][1]])] = -1
    else:
        location[0] += directions[inputVal][0]
        location[1] += directions[inputVal][1]
        distance += 1
        visited[tuple(location)] = distance
        stack.append(inputVal)

def optimize(visited, location):
    adjacent = [tuple([location[0] + 1, location[1]]), tuple([location[0] - 1, location[1]]), tuple([location[0], location[1] + 1]), tuple([location[0], location[1] - 1])]
    for adj in adjacent:
        if adj in visited:
            diff = visited[adj] - visited[location]
            if diff > 1:
                visited[adj] -= (diff - 1)
                optimize(visited, adj)

visited = {key:val for key, val in visited.items() if val != -1}

for v in visited:
    optimize(visited, v)

print(visited.values())