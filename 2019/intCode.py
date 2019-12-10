import sys

def resolveParameter(nums, index, parameter, relativeIndex):
    if parameter == '0':
        return nums[index]
    elif parameter == '1':
        return index
    elif parameter == '2':
        return nums[index] + relativeIndex
    else:
        return -1

def intCode(nums, inputs = [], i = 0):
    output = []
    relativeIndex = 0
    while True:
        opcode = nums[i] % 100
        parameter = int(nums[i] / 100)
        instString = '000'
        if parameter > 0:
            instString = str(parameter).zfill(3)[::-1]

        if opcode == 1:
            nums[resolveParameter(nums, i + 3, instString[2], relativeIndex)] = nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] + nums[resolveParameter(nums, i + 2, instString[1], relativeIndex)]
            i += 4
        elif opcode == 2:
            nums[resolveParameter(nums, i + 3, instString[2], relativeIndex)] = nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] * nums[resolveParameter(nums, i + 2, instString[1], relativeIndex)]
            i += 4
        elif opcode == 3:
            newInput = 0
            if len(inputs) > 0:
                newInput = inputs.pop(0)
            else:
                newInput = int(input("Input: "))
            nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] = newInput
            i += 2
        elif opcode == 4:
            output.append(nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)])
            i += 2
        elif opcode == 5:
            if nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] != 0:
                i = nums[resolveParameter(nums, i + 2, instString[1], relativeIndex)]
            else:
                i += 3
        elif opcode == 6:
            if nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] == 0:
                i = nums[resolveParameter(nums, i + 2, instString[1], relativeIndex)]
            else:
                i += 3
        elif opcode == 7:
            nums[resolveParameter(nums, i + 3, instString[2], relativeIndex)] = (1 if nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] < nums[resolveParameter(nums, i + 2, instString[1], relativeIndex)] else 0)
            i += 4
        elif opcode == 8:
            nums[resolveParameter(nums, i + 3, instString[2], relativeIndex)] = (1 if nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)] == nums[resolveParameter(nums, i + 2, instString[1], relativeIndex)] else 0)
            i += 4
        elif opcode == 9:
            relativeIndex += nums[resolveParameter(nums, i + 1, instString[0], relativeIndex)]
            i += 2
        elif opcode == 99:
            break
        else:
            print('ERROR, ABORTING')
            sys.exit(1)

    return output
