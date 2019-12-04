inputFile = open('./2019/day4input.txt', 'r')
input = inputFile.read()

#PART 1
inputParts = input.split('-')
lower = inputParts[0]
upper = inputParts[1]

lowerInt = int(lower)
upperInt = int(upper)

count = 0
found = set()

for i in range (5):
    for i1 in range (10):
        for i2 in range (i1, 10):
            for i3 in range (i2, 10):
                for i4 in range (i3, 10):
                    for i5 in range (i4, 10):
                        currentList = [str(i1), str(i2), str(i3), str(i4), str(i5)]
                        currentList.insert(i, currentList[i])
                        currentInt = int(''.join(currentList))
                        if currentInt >= lowerInt and currentInt <= upperInt:
                            if currentInt not in found:
                                found.add(currentInt)
                                count += 1

print("PART 1: ", count)

#PART 2
inputParts = input.split('-')
lower = inputParts[0]
upper = inputParts[1]

lowerInt = int(lower)
upperInt = int(upper)

count2 = 0
found2 = set()

for i in range (5):
    for i1 in range (10):
        for i2 in range (i1, 10):
            if (i == 0 or i == 1) and i1 == i2:
                continue
            for i3 in range (i2, 10):
                if (i == 1 or i == 2) and i2 == i3:
                    continue
                for i4 in range (i3, 10):
                    if (i == 2 or i == 3) and i3 == i4:
                        continue
                    for i5 in range (i4, 10):
                        if (i == 3 or i == 4) and i4 == i5:
                            continue
                        currentList = [str(i1), str(i2), str(i3), str(i4), str(i5)]
                        currentList.insert(i, currentList[i])
                        currentInt = int(''.join(currentList))
                        if currentInt >= lowerInt and currentInt <= upperInt:
                            if currentInt not in found2:
                                found2.add(currentInt)
                                count2 += 1

print("PART 2: ", count2)