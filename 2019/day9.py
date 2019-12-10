from intCode import intCode
inputFile = open('./2019/day9input.txt', 'r')
inputText = inputFile.read()

print('PART 1: ', intCode(inputText, [1]))
print('PART 2: ', intCode(inputText, [2]))