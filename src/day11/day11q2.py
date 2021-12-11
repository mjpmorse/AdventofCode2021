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
    allFlashed = False
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

                    # TODO: can this be done in a loop?
                    if x != 0:
                        octopusMap[x - 1][y] += 1
                    if x != (len(octopusMap) - 1):
                        octopusMap[x + 1][y] += 1
                    if y != 0:
                        octopusMap[x][y - 1] += 1
                    if y != (len(row) - 1):
                        octopusMap[x][y + 1] += 1
                    if x != 0 and y != 0:
                        octopusMap[x - 1][y - 1] += 1
                    if x != 0 and y != (len(row) - 1):
                        octopusMap[x - 1][y + 1] += 1
                    if x != (len(octopusMap) - 1) and y != 0:
                        octopusMap[x + 1][y - 1] += 1
                    if x != (len(octopusMap) - 1) and y != (len(row) - 1):
                        octopusMap[x + 1][y + 1] += 1

        if numberOfCycles > len(octopusMap)*len(octopusMap[0]):
            raise Exception("too many chain reactions")

    # update octopus > 9 to 0
    allFlashed = not any([0 in line for line in alreadyFlashed])

    for x, row in enumerate(alreadyFlashed):
        for y, element in enumerate(row):
            if element == 1:
                octopusMap[x][y] = 0

    return numberFlashes, allFlashed


ic(octopusMap) if debug else ""
totalFlashes = 0
count = 0
while True:
    count += 1
    if timeStep(octopusMap)[1]:
        break
    if count > 5000:
        raise Exception('More than 500 steps')


statement = (
    f"After {count} steps, they all flashed together"
)
print(statement)
