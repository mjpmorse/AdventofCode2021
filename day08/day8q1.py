from icecream import ic

debug = False
inputValues = []
outputValues = []

with open('data/data_q8.txt', 'r') as f:
    for line in f:
        line = line.split(' | ')
        tmpI = [x.strip() for x in line[0].split(' ')]
        tmpO = [x.strip() for x in line[1].split(' ')]
        inputValues.append(tmpI)
        outputValues.append(tmpO)

outputLenDict = {x: 0 for x in range(0, 10)}

for output in outputValues:
    for entry in output:
        entryLen = len(set(entry))
        outputLenDict[entryLen] += 1

oneFourSevenEight =\
    outputLenDict[2] +\
    outputLenDict[4] +\
    outputLenDict[3] +\
    outputLenDict[7]

ic(outputLenDict) if debug else ""

statement = (
    "The number of Ones, Fours, "
    "Sevens, Eights is: "
    f"{oneFourSevenEight}"
    )
print(statement)
