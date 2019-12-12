from intCode import intCode
inputFile = open('./2019/day9input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr)) + [0]*10000

print('PART 1: ', intCode(nums, [1])[0][0])
print('PART 2: ', intCode(nums, [2])[0][0])