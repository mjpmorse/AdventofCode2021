import numpy as np
from icecream import ic

debug = False
numberOfDays = 256

with open('data/data_q6.txt', 'r') as f:
    fishList = f.readlines(-1)[0]
    fishList = fishList.split(',')

fishList = np.array(fishList, dtype=int)
fishDict = np.unique(fishList, return_counts=True)
fishDict = dict(zip(*fishDict))
for timer in range(9):
    if not fishDict.get(timer):
        fishDict[timer] = 0

# might not need this
fishDict[-1] = 0

ic(fishDict) if debug else ""
for day in range(1, numberOfDays + 1):
    for timer in range(9):
        # move everything down one
        fishDict[timer - 1] = fishDict[timer]

    numberNewFish = fishDict[-1]
    fishDict[8] = numberNewFish
    fishDict[6] = fishDict[6] + fishDict[-1]
    fishDict[-1] = 0
    fishList[fishList == -1] = 6
    ic(f"After {day} days: {fishDict}") if debug else ""

numberOfFish = 0
for timer, fish in fishDict.items():
    numberOfFish += fish

statement = (f"After {numberOfDays} days there are "
             f"{numberOfFish} fish.")

print(statement)
