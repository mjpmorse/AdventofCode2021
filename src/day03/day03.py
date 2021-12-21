import numpy as np
from icecream import ic


def readData(file):
    with open(file, 'r') as f:
        data_ = np.loadtxt(f, dtype=str)
    return data_


def partOne(file):
    gamma = bin(0)
    epsilon = bin(1)
    data_ = readData(file)
    data = []
    for line in data_:
        data.append([int(x) for x in line])
    data = np.array(data)
    gamma = np.floor(2 * np.sum(data, axis=0))/len(data)
    gamma = gamma.astype(int).astype(str)
    gamma = int(''.join(gamma), base=2)
    # bit flip gamma to get epsilon
    num_digits = data.shape[1]
    base_2 = f"0b{'1' * num_digits}"
    epsilon = gamma ^ int(base_2, base=2)

    return epsilon * gamma


def one_zero_count(arry):
    one_count = np.count_nonzero(arry, axis=0)
    zero_count = arry.shape[0] * np.ones_like(one_count) - one_count
    target = one_count >= zero_count
    return one_count, zero_count, target


def partTwo(file):

    data = []
    data_ = readData(file)
    for line in data_:
        data.append([int(x) for x in line])

    data = np.array(data)
    one_count = np.count_nonzero(data, axis=0)
    zero_count = data.shape[0] * np.ones_like(one_count) - one_count
    ic(f'The number of ones are : {one_count}')
    ic(f'The number of zeros are: {zero_count}')
    ic(f'For a total of {one_count + zero_count}')

    oxygen_reading = np.copy(data)
    carbon_dioxide_reading = np.copy(data)

    # grab bit
    for bit in range(data.shape[1]):
        if oxygen_reading.shape[0] > 1:
            _, _, target_O2 = one_zero_count(oxygen_reading)
            oxygen_mask = (oxygen_reading[:, bit] == target_O2[bit])
            oxygen_reading = oxygen_reading[oxygen_mask]

        if carbon_dioxide_reading.shape[0] > 1:
            _, _, target_cO2 = one_zero_count(carbon_dioxide_reading)
            carbon_dioxide_mask = (
                carbon_dioxide_reading[:, bit]
                != target_cO2[bit])
            carbon_dioxide_reading =\
                carbon_dioxide_reading[carbon_dioxide_mask]

    oxygen_reading = ''.join(oxygen_reading.flatten().astype(str))
    oxygen_reading = int(oxygen_reading, base=2)

    carbon_dioxide_reading = ''.join(
        carbon_dioxide_reading.flatten().astype(str))
    carbon_dioxide_reading = int(carbon_dioxide_reading, base=2)

    return oxygen_reading*carbon_dioxide_reading
