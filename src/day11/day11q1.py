from icecream import ic

debug = False
file = 'data_q11_dummy.txt' if debug else 'data_q11.txt'
octopusMap = []

with open(f'data/{file}', 'r') as f:
    for line in f:
        line = [int(x) for x in line.strip()]
        octopusMap.append(line)


def timeStep(octopusMap):

    alreadyFlashed = []

    numberFlashes = 0
    # update each octopus by one
    for x, row in enumerate(octopusMap):
        alreadyFlashed.append([0 for x in row])
        for y, element in enumerate(row):
            octopusMap[x][y] += 1

    anyFlashThisTime = True
    numberOfCycles = 0
    while anyFlashThisTime:
        # check if greater than 9 and already flash:
        anyFlashThisTime = False
        numberOfCycles += 1
        for x, row in enumerate(octopusMap):
            for y, element in enumerate(row):
                if (element > 9) and (alreadyFlashed[x][y] == 0):
                    anyFlashThisTime = True
                    numberFlashes += 1
                    alreadyFlashed[x][y] = 1
                    ic(f"row: {x} column: {y} just fired") if debug else ""

                    for xOffset in [0, 1, -1]:
                        for yOffset in [0, 1, -1]:
                            if xOffset == 0 and yOffset == 0:
                                # we do not want to do anything
                                # on this square.
                                continue
                            condition = (
                                x + xOffset in range(0, len(octopusMap))
                                and
                                y + yOffset in range(0, len(row))
                            )
                            if condition:
                                octopusMap[x + xOffset][y + yOffset] += 1

        if numberOfCycles > len(octopusMap)*len(octopusMap[0]):
            raise Exception("too many chain reactions")

    # update octopus > 9 to 0
    for x, row in enumerate(alreadyFlashed):
        for y, element in enumerate(row):
            if element == 1:
                octopusMap[x][y] = 0
    return numberFlashes


ic(octopusMap) if debug else ""
totalFlashes = 0
for step in range(100):
    totalFlashes += timeStep(octopusMap)
    if step % 10 == 0 and debug:
        ic(octopusMap)

statement = (
    f"There were {totalFlashes} flahes"
)
print(statement)
