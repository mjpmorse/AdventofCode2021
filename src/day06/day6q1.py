import numpy as np
from icecream import ic

debug = False
numberOfDays = 80

with open('data/data_q6.txt', 'r') as f:
    fishList = f.readlines(-1)[0]
    fishList = fishList.split(',')

fishList = np.array(fishList, dtype=int)

ic(f"Initial state: {fishList}") if debug else ""

for day in range(1, numberOfDays + 1):
    fishList = fishList - 1
    numberNewFish = len(fishList[fishList == -1])

    if numberNewFish > 0:
        newFishList = 8 * np.ones(numberNewFish, dtype=int)
        fishList = np.append(fishList, newFishList)

    fishList[fishList == -1] = 6
    ic(f"After {day} days: {fishList}") if debug else ""

statement = (f"After {numberOfDays} days there are "
             f"{len(fishList)} fish.")

print(statement)
