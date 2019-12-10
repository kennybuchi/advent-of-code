from intCode import intCode
inputFile = open('./2019/day5input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr))

#PART 1 & 2 



print(intCode(nums))