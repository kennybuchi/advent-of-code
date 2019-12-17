inputFile = open('./2019/day16input.txt', 'r')
inputText = inputFile.read()

numList = list(map(int, inputText))

#PART 1

def FFT(inputList, pattern, phases):
    nums = inputList
    for uselessIterator in range(phases):
        newList = nums.copy()
        for i in range(len(nums)):
            listIt = 0
            patternIt = 0
            patternRepeat = 1
            numSum = 0
            while listIt < len(nums):
                if patternRepeat == i + 1:
                    patternIt += 1
                    patternIt %= len(pattern)
                    patternRepeat = 0
                numSum += nums[listIt] * pattern[patternIt]
                listIt += 1
                patternRepeat += 1
            newList[i] = abs(numSum) % 10
        nums = newList.copy()

    return nums

        

phases = 1
pattern = [0, 1, 0, -1]

finalList = FFT(numList, pattern, phases)

finalStr = ''
for i in range(8):
    finalStr += str(finalList[i])

print('PART 1: ' + finalStr)

#PART 2

numList = list(map(int, inputText)) * 10000

finalList = FFT(numList, pattern, phases)

offsetStr = ''
for i in range(7):
    offsetStr += str(finalList[i])
offset = int(offsetStr)

finalStr = ''
for i in range(offset, offset + 8):
    finalStr += str(finalList[i])

print(FFT(numList, pattern, phases))