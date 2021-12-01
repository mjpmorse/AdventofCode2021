import numpy as np
from icecream import ic

with open('day01/data_q1.txt', 'r') as f:
    data = np.loadtxt(f, dtype=int)

diff = data[1:] - data[:-1]
ic(f"{data[:4]}")
ic(f"{diff[0]} =  {data[1:][0]} - {data[:-1][0]}")
print(len(diff[diff > 0]))
