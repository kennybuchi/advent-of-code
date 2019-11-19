inputFile = open('/home/klee/aoc/2017/day2input.txt', 'r')
input = inputFile.read()

#PART 1

checksum = 0
lines = input.splitlines()

for line in lines:
    nums = line.split()
    min = 99999999999
    max = -99999999999

    for num in nums:
        num = int(num)
        if num < min:
            min = num
        if num > max:
            max = num
    
    checksum += (max - min)

print(checksum)

#PART 2

checksum = 0
lines = input.splitlines()

for line in lines:
    nums = line.split()

    for i in range(len(nums) - 1):
        found = False
        num1 = int(nums[i])
        for j in range(i + 1, len(nums)):
            num2 = int(nums[j])
            if num1 >= num2 and num1 % num2 == 0:
                checksum += int(num1 / num2)
                found = True
                break
            if num1 < num2 and num2 % num1 == 0:
                checksum += int(num2 / num1)
                found = True
                break
        if found == True:
            break

print(checksum)