import math
inputFile = open('./2019/day8input.txt', 'r')
inputText = inputFile.read()

x_size, y_size = 25, 6
layerSize = x_size * y_size

numLayers = math.ceil(len(inputText) / layerSize)

layers = [ inputText[i:i + layerSize] for i in range(0, len(inputText), layerSize)]


layerIndex = numLayers + 1
minZeros = layerSize
for i in range(len(layers)):
    count = layers[i].count('0')
    if count < minZeros:
        layerIndex = i
        minZeros = count

print('PART 1: ', layers[layerIndex].count('1') * layers[layerIndex].count('2'))

#PART 2

output = ''
for i in range(layerSize):
    for j in range(numLayers):
        if layers[j][i] == '0':
            output += ' '
            break
        if layers[j][i] == '1':
            output += '#'
            break
outputGrid = [ output[i:i + x_size] for i in range(0, len(output), x_size)]

for line in outputGrid:
    print(line)