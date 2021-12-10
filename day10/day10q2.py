from icecream import ic

debug = False
navSubSystem = []
openChars = ('(', '{', '[', '<')
closeChars = (')', '}', ']', '>')
corruptLines = []
incompleteLines = []
navSubSystemCorrected = []
scores = []
value = 0
valueDict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

file = 'data_q10_dummy.txt' if debug else 'data_q10.txt'

with open(f'data/{file}', 'r') as f:
    for line in f:
        line = [x for x in line.strip()]
        navSubSystem.append(line)

ic([''.join(line) for line in navSubSystem]) if debug else ""

'''
Part 1:
Find the corrupt lines:
Find which closing char is incorrect:

'''

for line in navSubSystem:
    correctedLine = line[:]
    corrupt = False
    lineOpening = [x for x in line if (x in openChars)]
    lineClosing = [x for x in line if (x in closeChars)]

    for closChar in lineClosing:
        positionInString = line.index(closChar)
        correspondingOpenChar = openChars[closeChars.index(closChar)]
        correctClosingChar = closeChars[openChars.index(correspondingOpenChar)]

        if positionInString == 0:
            raise Exception(f"line {''.join(line)} started with {closChar}")

        # these will not be equal if the closing char is incorrect
        if line[positionInString - 1] != correspondingOpenChar:
            corruptLines.append(correctedLine)
            corrupt = True
            break
        else:
            # If correct, pop the pair from the line
            line.pop(positionInString)
            line.pop(positionInString - 1)

    # If our line was incomplete, we will now have an empty
    # list for line since we popped everything out unless
    # the line was incomplete
    if (len(line) != 0) and (not corrupt):
        # what is left needs to be closed
        ic(''.join(line)) if debug else ""
        localScore = 0
        for openChar in line[::-1]:
            closingChar = closeChars[openChars.index(openChar)]
            localScore = 5 * localScore + valueDict[closingChar]
        ic(f"{localScore}") if debug else ""
        ic(f"{scores}") if debug else ""
        scores.append(localScore)

scores.sort()
statement = (
    f"The middle score is {scores[(len(scores)-1) // 2]}"
)
print(statement)
