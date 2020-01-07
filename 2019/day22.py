import collections

inputFile = open('./2019/day22input.txt', 'r')
inputText = inputFile.read()
inputLines = inputText.splitlines()

def cutDeck(deck, num):
    if num >= 0:
        for i in range(num):
            deck.append(deck.popleft())
    else:
        for i in range(abs(num)):
            deck.appendleft(deck.pop())

def incDeck(deck, deckSize, num):
    deckList = [-1] * deckSize
    index = 0
    for i in range(deckSize):
        deckList[index] = deck.popleft()
        index = (index + num) % deckSize
    return collections.deque(deckList)


new = 'deal into new stack'
cut = 'cut '
inc = 'deal with increment '

deckSize = 10007
findCard = 2019
deck = collections.deque()
for i in range(deckSize):
    deck.append(i)

num = 0

for line in inputLines:
    if line.startswith(new):
        deck.reverse()
    elif line.startswith(cut):
        num = int(line[len(cut):])
        cutDeck(deck, num)
    elif line.startswith(inc):
        num = int(line[len(inc):])
        deck = incDeck(deck, deckSize, num)

for i in range(deckSize):
    if deck.popleft() == 2019:
        print('PART 1: ', i)
        break

