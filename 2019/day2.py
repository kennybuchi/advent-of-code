import sys
inputFile = open('./2019/day2input.txt', 'r')
input = inputFile.read()

inputArr = input.split(',')
nums = list(map(int, inputArr))
i = 0

#PART 1

#Replace pos 1 with value 12, pos 2 with value 2
nums[1] = 12
nums[2] = 2

while True:
    if nums[i] == 1:
        nums[nums[i + 3]] = nums[nums[i + 1]] + nums[nums[i + 2]]
        i += 4
    elif nums[i] == 2:
        nums[nums[i + 3]] = nums[nums[i + 1]] * nums[nums[i + 2]]
        i += 4
    elif nums[i] == 99:
        break
    else:
        print('ERROR, ABORTING')
        sys.exit(1)

print(nums[0])

#PART 2

originalNums = list(map(int, inputArr))
goal = 19690720

def getNounAndVerb(originalNums, goal):
    for noun in range(100):
        for verb in range(100):
            nums = originalNums.copy()
            nums[1] = noun
            nums[2] = verb
            i = 0

            while True:
                if nums[i] == 1:
                    nums[nums[i + 3]] = nums[nums[i + 1]] + nums[nums[i + 2]]
                    i += 4
                elif nums[i] == 2:
                    nums[nums[i + 3]] = nums[nums[i + 1]] * nums[nums[i + 2]]
                    i += 4
                elif nums[i] == 99:
                    break
                else:
                    print('ERROR, ABORTING')
                    sys.exit(1)

            if nums[0] == goal:
                return 100 * noun + verb

print(getNounAndVerb(originalNums, goal))