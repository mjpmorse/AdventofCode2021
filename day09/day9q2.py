from icecream import ic
from typing import List, Tuple
debug = False
heightMap = []

file = 'data_q9_dummy.txt' if debug else 'data_q9.txt'
with open(f'data/{file}', 'r') as f:
    for line in f:
        line = [int(x) for x in line.strip()]
        heightMap.append(line)

ic(heightMap) if debug else ""
basinMap = []
for row in heightMap:
    basinMap.append([int(not x // 9) for x in row])

ic(basinMap) if debug else ""


def comparePoints(
        heightMap: List[List[int]],
        index: Tuple[int, int]) -> bool:

    check = True

    pointRow = index[0]
    pointColumn = index[1]
    point = heightMap[pointRow][pointColumn]

    mapDepth = len(heightMap) - 1
    mapWidth = len(heightMap[0]) - 1

    # check the point to the left if pointColumn != 0
    if pointColumn != 0:
        check *= (heightMap[pointRow][pointColumn - 1] > point)

    # check the point to the right if pointColumn != mapWidth
    if pointColumn != mapWidth:
        check *= (heightMap[pointRow][pointColumn + 1] > point)

    # check the point above if pointRow != 0
    if pointRow != 0:
        check *= (heightMap[pointRow - 1][pointColumn] > point)

    # check the point below if pointRow != mapDepth
    if pointRow != mapDepth:
        check *= (heightMap[pointRow + 1][pointColumn] > point)

    return check


def zerosAround(basinMap, row, column):
    count = 0
    mapDepth = len(basinMap) - 1
    mapWidth = len(basinMap[0]) - 1

    if basinMap[row][column] == 0:
        return count

    else:
        count += 1
        basinMap[row][column] = 0

    # if we are not on top, check above us
    if row != 0:
        count += zerosAround(basinMap, row - 1, column)

    # if we are not at bottom check below us
    if row != mapDepth:
        count += zerosAround(basinMap, row + 1, column)

    # if we are not on LHS check to our left
    if column != 0:
        count += zerosAround(basinMap, row, column - 1)

    # if we are not at the RHS check to our right
    if column != mapWidth:
        count += zerosAround(basinMap, row, column + 1)

    return count


ic("basin map before search") if debug else ""
ic(basinMap) if debug else ""

iterations = 0
basinList = []
maxBasinNumber = len(basinMap) * len(basinMap[0])
while any([1 in row for row in basinMap]):
    iterations += 1
    # find any value of 1 to start
    startingX = 0
    startingY = 0
    for x, row in enumerate(basinMap):
        for y, element in enumerate(row):
            if element == 1:
                startingY = y
                startingX = x
                break
        if 1 in row:
            break
    basinList.append(
        zerosAround(basinMap, startingX, startingY)
        )
    ic(basinMap) if debug else ""
    if iterations == maxBasinNumber:
        raise Exception("Too many basins")

basinList.sort(reverse=True)
product = 1
for basinDepth in basinList[:3]:
    product *= basinDepth
statement = (
    f"The product of the three largest basins is: {product}"
)
print(statement)
