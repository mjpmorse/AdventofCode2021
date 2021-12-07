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


def crabEngineering(positionChange: int):
    fuelCost = 0
    for change in range(1, positionChange + 1):
        fuelCost += change
    return fuelCost


globalIntergerMin = PossiblePositionMax - PossiblePositionMin
globalFuelMin = globalIntergerMin * crabEngineering(globalIntergerMin)


def absoluteResidual(initialPositions: List[int], middlePosition: int):
    totalAbsoluteResidual = 0
    for position in initialPositions:
        fuelCost = abs(position - middlePosition)
        totalAbsoluteResidual += crabEngineering(fuelCost)
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
