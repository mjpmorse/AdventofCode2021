from icecream import ic
from typing import List, Tuple
debug = False
navSubSystem = []
openChars = ('(', '{', '[', '<')
closeChars = (')', '}', ']', '>')
corruptLines = []
incompleteLines = []
navSubSystemCorrected = []
value = 0
valueDict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

incorrectCount = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
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
            ic(f"closing char {closChar} at index {positionInString}") if False else ""
            ic(f"{''.join(line)}") if False else ""
            ic(f"Expected {correctClosingChar}, found {closChar}") if False else ""
            # correctedLine[positionInString] == correctClosingChar
            incorrectCount[closChar] += 1

            # we only want to add the first one right now
            break
        else:
            # If correct, pop the pair from the line
            line.pop(positionInString)
            line.pop(positionInString - 1)

ic(incorrectCount)
for bracket, count in incorrectCount.items():
    value += count * valueDict[bracket]

statement = (
    f"the total syntax error score for the errors is {value}"
)

print(statement)
