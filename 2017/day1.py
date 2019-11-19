inputFile = open('./2017/day1input.txt', 'r')
input = inputFile.read()

#PART 1

captcha = 0

for i in range(len(input)):
    if input[i] == input[i - 1]:
        captcha += int(input[i])

print('PART 1:', captcha)

#PART 2

captcha = 0
offset = int(len(input) / 2) 

for i in range(offset):
    if input[i] == input[i + offset]:
        captcha += (int(input[i]) * 2)

print('PART 2:', captcha)