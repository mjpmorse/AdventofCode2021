import numpy as np
from icecream import ic

window_size = 3
window = np.ones(window_size, dtype=int)

data = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])

with open('day01/data_q1.txt', 'r') as f:
    data = np.loadtxt(f, dtype=int)

data_sum = np.convolve(data, window, 'valid')

diff = data_sum[1:] - data_sum[:-1]
ic(f"{data_sum}")
ic(f"{diff[0]} =  {data_sum[1:][0]} - {data_sum[:-1][0]}")
print(len(diff[diff > 0]))