from intCode import intCode
inputFile = open('./2019/day5input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr))

#PART 1 & 2 

i = 0
output = intCode(nums, [1], i)
print('PART 1: ', output[0][-1])
    
nums = list(map(int, inputArr))
print('PART 2: ', intCode(nums, [5])[0][0])