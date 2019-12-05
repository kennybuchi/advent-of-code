import sys
inputFile = open('./2019/day5input.txt', 'r')
inputText = inputFile.read()

inputArr = inputText.split(',')
nums = list(map(int, inputArr))

#PART 1 & 2 (makes more sense to combine parts for this problem)
#COPIED FROM DAY2

def resolveParameter(nums, index, parameter):
    return index if parameter == '1' else nums[index]

i = 0
while True:
    opcode = nums[i] % 100
    parameter = int(nums[i] / 100)
    instString = '00'
    if parameter > 0:
        instString = str(parameter).zfill(3)[::-1]

    if opcode == 1:
        nums[nums[i + 3]] = nums[resolveParameter(nums, i + 1, instString[0])] + nums[resolveParameter(nums, i + 2, instString[1])]
        i += 4
    elif opcode == 2:
        nums[nums[i + 3]] = nums[resolveParameter(nums, i + 1, instString[0])] * nums[resolveParameter(nums, i + 2, instString[1])]
        i += 4
    elif opcode == 3:
        nums[nums[i + 1]] = int(input("Input: "))
        i += 2
    elif opcode == 4:
        # print('opcode: ', opcode, ', ', nums[i])
        print('Output: ', nums[resolveParameter(nums, i + 1, instString[0])])
        i += 2
    elif opcode == 5:
        if nums[resolveParameter(nums, i + 1, instString[0])] != 0:
            i = nums[resolveParameter(nums, i + 2, instString[1])]
        else:
            i += 3
    elif opcode == 6:
        if nums[resolveParameter(nums, i + 1, instString[0])] == 0:
            i = nums[resolveParameter(nums, i + 2, instString[1])]
        else:
            i += 3
    elif opcode == 7:
        nums[nums[i + 3]] = (1 if nums[resolveParameter(nums, i + 1, instString[0])] < nums[resolveParameter(nums, i + 2, instString[1])] else 0)
        i += 4
    elif opcode == 8:
        nums[nums[i + 3]] = (1 if nums[resolveParameter(nums, i + 1, instString[0])] == nums[resolveParameter(nums, i + 2, instString[1])] else 0)
        i += 4
    elif opcode == 99:
        break
    else:
        print('ERROR, ABORTING')
        sys.exit(1)