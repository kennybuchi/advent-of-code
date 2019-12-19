from intCode import intCode

inputFile = open('./2019/day19input.txt', 'r')
inputText = inputFile.read()
inputArr = inputText.split(',')
nums = list(map(int, inputArr)) + [0]*100

# #PART 1
count = 0
x, y = 50, 50

for i in range(x):
    for j in range(y):
        if intCode(nums.copy(), [i, j])[0][0] == 1:
            count += 1

print('PART 1: ', count)


#PART 2

x, y = 0, 1000


while True:
    x = int(y/2)
    while intCode(nums.copy(), [x, y])[0][0] == 0:
        x += 1
    if intCode(nums.copy(), [x + 99, y - 99])[0][0] == 1:
        break
    y += 1

print('PART 2: ', (x*10000)+(y - 99))