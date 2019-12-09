import sys

def resolveParameter(nums, index, parameter):
    return index if parameter == '1' else nums[index]

def intCode(inputText, inputs = []):
    inputArr = inputText.split(',')
    nums = list(map(int, inputArr))
    output = []
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
            newInput = 0
            if len(inputs) > 0:
                newInput = inputs.pop(0)
            else:
                newInput = int(input("Input: "))
            nums[nums[i + 1]] = newInput
            i += 2
        elif opcode == 4:
            output.append(nums[resolveParameter(nums, i + 1, instString[0])])
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

    return output
