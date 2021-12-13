from typing import List, Tuple

debug = True


def readInstructions(file):
    dotLocation = []
    foldInstruction = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if ',' in line:
                line = tuple(int(loc) for loc in line.split(','))
                dotLocation.append(line)
            elif "fold along x=" in line:
                line = (int(line.split('=')[-1]), 0)
                foldInstruction.append(line)
            elif "fold along y=" in line:
                line = (0, int(line.split('=')[-1]))
                foldInstruction.append(line)

    return dotLocation, foldInstruction


def makeDotMatrix(dotLocation: List[Tuple]) -> List[List[int]]:
    width = 0
    height = 0
    for dot in dotLocation:
        if dot[0] + 1 > width:
            width = dot[0] + 1
        if dot[1] + 1 > height:
            height = dot[1] + 1

    dotMatrix = [[0] * width for x in range(height)]

    for dot in dotLocation:
        dotMatrix[dot[1]][dot[0]] = 1
    return dotMatrix


def foldDotMatrix(dotMatrix: List[List[int]],
                  foldInstruction: Tuple) -> List[List[int]]:
    width = len(dotMatrix[0])
    height = len(dotMatrix)

    # fold along x
    if foldInstruction[1] == 0:
        newWidth = foldInstruction[0]
        newdotMatrix = [[0] * newWidth for x in range(height)]
        xRange = range(0, newWidth)
        yRange = range(0, height)

    # fold along y
    if foldInstruction[0] == 0:
        newHeight = foldInstruction[1]
        newdotMatrix = [[0] * width for x in range(newHeight)]
        xRange = range(0, width)
        yRange = range(0, newHeight)

    for y in yRange:
        for x in xRange:
            newdotMatrix[y][x] = dotMatrix[y][x]

    if foldInstruction[1] == 0:
        for y in range(0, height):
            for x in range(newWidth + 1, width):
                xOffSet = x - newWidth
                newXLocation = newWidth - xOffSet
                newdotMatrix[y][newXLocation] =\
                    int(dotMatrix[y][x]
                        or newdotMatrix[y][newXLocation])

    elif foldInstruction[0] == 0:
        for y in range(newHeight + 1, height):
            for x in range(0, width):
                yOffSet = y - newHeight
                newYLocation = newHeight - yOffSet
                newdotMatrix[newYLocation][x] =\
                    int(dotMatrix[y][x]
                        or newdotMatrix[newYLocation][x])

    return newdotMatrix


def partOne(file):
    dotLocation, instructions = readInstructions(file)
    dotMatrix = makeDotMatrix(dotLocation)
    dotMatrix = foldDotMatrix(dotMatrix, instructions[0])

    numDots = 0
    for row in dotMatrix:
        numDots += sum(row)

    statement = (
        f'There are {numDots} dots visible'
    )
    print(statement)
    return numDots


def partTwo(file):
    dotLocation, instructions = readInstructions(file)
    dotMatrix = makeDotMatrix(dotLocation)
    for instruction in instructions:
        dotMatrix = foldDotMatrix(dotMatrix, instruction)

    for row in dotMatrix:
        code = [str(x).replace('1', '#') for x in row]
        code = [x.replace('0', ' ') for x in code]
        print(''.join(code))

    return dotMatrix


partOne('data/data_q13.txt')
partTwo('data/data_q13.txt')
