'''
Part one of this question is to find a value which minimizes 
the sum of the difference to other values.
'''

from icecream import ic
from typing import List

with open('data/data_q7.txt', 'r') as f:
    crabList = f.readlines(-1)[0]
    crabList = crabList.split(',')

debug = False
numberOfDays = 80

crabList = [int(i) for i in crabList]
PossiblePositionMin = min(crabList)
PossiblePositionMax = max(crabList)

globalIntergerMin = PossiblePositionMax - PossiblePositionMin
globalFuelMin = len(crabList) * globalIntergerMin


def absolute_residual(initialPositions: List[int], middlePosition: int):
    totalAbsoluteResidual = 0
    for position in initialPositions:
        totalAbsoluteResidual += abs(position - middlePosition)
    return totalAbsoluteResidual


for position in range(PossiblePositionMin, PossiblePositionMax + 1):
    nextGuess = absolute_residual(crabList, position)
    if nextGuess < globalFuelMin:
        globalIntergerMin = position
        globalFuelMin = nextGuess

statement = (f"The best position is {globalIntergerMin} "
             f"with a total of {globalFuelMin} fuel used")
print(statement)
