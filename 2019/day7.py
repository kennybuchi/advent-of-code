from intCode import intCode
from itertools import permutations
inputFile = open('./2019/day7input.txt', 'r')
inputText = inputFile.read()

#PART 1

iters = list(permutations(range(0, 5)))
maxOut = 0

for it in iters:
    output = 0
    for i in it:
        output = intCode(inputText, [i, output])[0]
    if output > maxOut:
        maxOut = output

print('PART 1: ', maxOut)