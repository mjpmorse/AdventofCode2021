import numpy as np
from icecream import ic

debug = False


coordinatesStart = []
coordinatesEnd = []
maxOverlap = 2

with open('day05/data_q5.txt', 'r') as f:
    for line in f:
        line = line.split('->')
        coordinatesStart.append(line[0].split(','))
        coordinatesEnd.append(line[1].split(','))

coordinatesStart = np.array(coordinatesStart).astype(int)
coordinatesEnd = np.array(coordinatesEnd).astype(int)

maxX = max(
    coordinatesStart[:, 0].max(),
    coordinatesEnd[:, 0].max()) + 1

maxY = max(
    coordinatesStart[:, 1].max(),
    coordinatesEnd[:, 1].max()) + 1

# set up a grid the same shape as the field
# we are c-like so y, x
# else we are transposed
grid = np.zeros((maxY, maxX), dtype=int)

'''
iterate over the start and end points,
increasing the field count when the start or end points
are equal
'''
for startPoint, endPoint in zip(coordinatesStart, coordinatesEnd):
    startX = startPoint[0]
    endX = endPoint[0]
    startY = startPoint[1]
    endY = endPoint[1]
    dx = endX - startX
    dy = endY - startY

    # we only care about straight lines for now
    if dx == 0 or dy == 0:
        if dx == 0:
            yToIncrease = np.linspace(startY, endY, abs(dy) + 1, dtype=int)
            numPoints = len(yToIncrease)
            xToIncrease = startX * np.ones(numPoints, dtype=int)
        elif dy == 0:
            xToIncrease = np.linspace(startX, endX, abs(dx) + 1, dtype=int)
            numPoints = len(xToIncrease)
            yToIncrease = startY * np.ones(numPoints, dtype=int)

        xToIncrease = xToIncrease.reshape(-1, 1)
        yToIncrease = yToIncrease.reshape(-1, 1)
        toChange = np.hstack((xToIncrease, yToIncrease))
        ic(xToIncrease) if debug else ""

        for point in toChange:
            x = point[0]
            y = point[1]
            grid[y, x] = grid[y, x] + 1

ic(grid) if debug else ""
ic(grid[grid >= maxOverlap]) if debug else ""

numberOfMaxOverlap = len(grid[grid >= maxOverlap])

statement = (
    f"At {numberOfMaxOverlap} points at least {maxOverlap} "
    f"lines overlap"
    )
print(statement)
