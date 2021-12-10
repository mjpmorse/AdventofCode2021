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

riskLevel = 0

for row in range(len(heightMap)):
    for column in range(len(heightMap[1])):
        localMin = comparePoints(heightMap, (row, column))
        if localMin:
            riskLevel += (heightMap[row][column] + 1)
statement = (
    "The sum of the risk levels for all the "
    f"lowest points is {riskLevel}"
    )
print(statement)
