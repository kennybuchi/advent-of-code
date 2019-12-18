from intCode import intCode

inputFile = open('./2019/day17input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr)) + [0]*10000

#PART 1
output = intCode(nums)[0]

row = 0
grid = ['']

for num in output:
    if num == 10:
        row += 1
        grid.append('')
    else:
        grid[row] += chr(num)

alignSum = 0

# -- remove the extra lines -- 
while grid[-1] == '':
    grid.pop()

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == '#' and grid[i+1][j] == '#' and grid[i-1][j] == '#' and grid[i][j+1] == '#' and grid[i][j-1] == '#':
            alignSum += i*j

print('PART 1: ' + str(alignSum))

#PART 2

nums = list(map(int, inputArr)) + [0]*10000
nums[0] = 2

#this was done manually..
mainMovement = 'A,B,A,C,A,B,C,A,B,C\n'
A = 'R,12,R,4,R,10,R,12\n'
B = 'R,6,L,8,R,10\n'
C = 'L,8,R,4,R,4,R,6\n'

inputStr = mainMovement + A + B + C + 'n\n'
input2 = list(map(ord, inputStr))

dust = intCode(nums, list(input2))[0][-1]
print('PART 2: ' + str(dust))