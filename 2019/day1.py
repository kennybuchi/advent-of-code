inputFile = open('./2019/day1input.txt', 'r')
input = inputFile.read()

#PART 1

inputLines = input.splitlines()
fuelTotal = 0

for line in inputLines:
    num = int(line)
    fuelTotal += ( int(num / 3) - 2 )

print('PART 1: ', fuelTotal)

#PART 2

fuelTotal = 0

for line in inputLines:
    num = int(line)
    moduleFuel = ( int(num / 3) - 2 )

    while moduleFuel > 0:
        fuelTotal += moduleFuel
        moduleFuel = ( int(moduleFuel / 3) - 2 )

print('PART 1: ', fuelTotal)