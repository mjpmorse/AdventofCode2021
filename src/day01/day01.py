import numpy as np
from icecream import ic

def readData(file):
    with open(file, 'r') as f:
        data = np.loadtxt(f, dtype=int)
    return data

def partOne(file):
    data = readData(file)
    diff = data[1:] - data[:-1]
    diffG0 = diff[diff > 0]
    statement = (
        f'There are {len(diffG0)} greater than 0'
    )
    print(statement)
    return len(diffG0)


def partTwo(file):
    window_size = 3
    window = np.ones(window_size, dtype=int)
    with open(file, 'r') as f:
        data = np.loadtxt(f, dtype=int)

    data_sum = np.convolve(data, window, 'valid')

    diff = data_sum[1:] - data_sum[:-1]
    diffG0 = diff[diff > 0]
    print(len(diffG0))
    return len(diffG0)
