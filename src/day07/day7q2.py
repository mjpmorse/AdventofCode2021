from typing import List
from icecream import ic

with open('data/data_q7.txt', 'r') as f:
    crabList = f.readlines(-1)[0]
    crabList = crabList.split(',')

debug = False
numberOfDays = 80

crabList = [int(i) for i in crabList]
PossiblePositionMin = min(crabList)
PossiblePositionMax = max(crabList)


globalIntergerMin = PossiblePositionMax - PossiblePositionMin
globalFuelMin = (globalIntergerMin**2 + globalIntergerMin) * globalIntergerMin


def absoluteResidual(initialPositions: List[int], middlePosition: int):
    totalAbsoluteResidual = 0
    for position in initialPositions:
        fuelCost = abs(position - middlePosition)
        totalAbsoluteResidual += int((fuelCost**2 + fuelCost)/2)
    return totalAbsoluteResidual


for position in range(PossiblePositionMin, PossiblePositionMax + 1):
    nextGuess = absoluteResidual(crabList, position)
    ic(f"position: {position}, cost: {nextGuess}") if debug else ""

    if nextGuess < globalFuelMin:
        globalIntergerMin = position
        globalFuelMin = nextGuess

statement = (f"The best position is {globalIntergerMin} "
             f"with a total of {globalFuelMin} fuel used")
print(statement)
