import re
import functools
inputFile = open('./2019/day12input.txt', 'r')
inputText = inputFile.read()

inputLines = inputText.splitlines()

class Moon:
    def __init__ (self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.neighbors = []
    
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def updatePosition(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

    def updateVelocity(self):
        for neighbor in self.neighbors:
            for i in range(len(self.position)):
                if self.position[i] < neighbor.position[i]:
                    self.velocity[i] += 1
                elif self.position[i] > neighbor.position[i]:
                    self.velocity[i] -= 1

    def getPosition(self):
        return tuple(self.position)

    def getVelocity(self):
        return tuple(self.velocity)

    def getKineticEnergy(self):
        kineticEnergy = 0
        for vel in self.velocity:
            kineticEnergy += abs(vel)
        return kineticEnergy

    def getPotentialEnergy(self):
        potentialEnergy = 0
        for pos in self.position:
            potentialEnergy += abs(pos)
        return potentialEnergy

    def getTotalEnergy(self):
        return self.getKineticEnergy() * self.getPotentialEnergy()


#PART 1

moons = []
finalStep = 1000

for line in inputLines:
    position = list(map(int, re.sub(r'[^0-9\-,\n]', '', line).split(',')))
    moon = Moon(position, [0, 0, 0])
    moons.append(moon)
    
for moon in moons:
    for moon2 in moons:
        if moon != moon2:
            moon.addNeighbor(moon2)

for i in range(finalStep):
    for moon in moons:
        moon.updateVelocity()
    for moon in moons:
        moon.updatePosition()

energySum = 0
for moon in moons:
    energySum += moon.getTotalEnergy()

print('PART 1: ', energySum)

#PART 2

def getMoonsTuple(moons):
    l = []
    for moon in moons:
        l.append(moon.getPosition())
        l.append(moon.getVelocity())
    return tuple(l)

moons = []
finalStep = 1000

for line in inputLines:
    position = list(map(int, re.sub(r'[^0-9\-,\n]', '', line).split(',')))
    moon = Moon(position, [0, 0, 0])
    moons.append(moon)
    
for moon in moons:
    for moon2 in moons:
        if moon != moon2:
            moon.addNeighbor(moon2)

steps = [0, 0, 0]
step = 0
moonTuple = getMoonsTuple(moons)

while 0 in steps:
    step += 1
    for moon in moons:
        moon.updateVelocity()
    for moon in moons:
        moon.updatePosition()
    newTuple = getMoonsTuple(moons)  
    for i in range(3):
        if steps[i] != 0:
            continue
        cycle = True
        for j in range(len(moons) * 2):
            if moonTuple[j][i] != newTuple[j][i]:
                cycle = False
                break
        if cycle:
            steps[i] = step

# ~~~ using LCM code from https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return functools.reduce(lcm, args)
# ~~~

print(lcmm(steps[0], steps[1], steps[2]))