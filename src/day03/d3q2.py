import numpy as np
from icecream import ic


gamma = bin(0)
epsilon = bin(1)
# TODO: Can this be done with bit minupulation?
# exclusive or
data = []
data_ = []
with open('data/data_q3.txt', 'r') as f:
    data_ = np.loadtxt(f, dtype=str)
if False:
    data_ = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
for line in data_:
    data.append([int(x) for x in line])

data = np.array(data)
data_T = data.T

one_count = np.count_nonzero(data, axis=0)
zero_count = data.shape[0] * np.ones_like(one_count) - one_count
ic(f'The number of ones are : {one_count}')
ic(f'The number of zeros are: {zero_count}')
ic(f'For a total of {one_count + zero_count}')

oxygen_reading = np.copy(data)
carbon_dioxide_reading = np.copy(data)


def one_zero_count(arry):
    one_count = np.count_nonzero(arry, axis=0)
    zero_count = arry.shape[0] * np.ones_like(one_count) - one_count
    target = one_count >= zero_count
    return one_count, zero_count, target


# grab bit
for bit in range(data.shape[1]):
    if oxygen_reading.shape[0] > 1:
        _, _, target_O2 = one_zero_count(oxygen_reading)
        ic(f"bit {bit} has a target of {target_O2[bit]}")
        oxygen_mask = (oxygen_reading[:, bit] == target_O2[bit])
        oxygen_reading = oxygen_reading[oxygen_mask]

    if carbon_dioxide_reading.shape[0] > 1:
        _, _, target_cO2 = one_zero_count(carbon_dioxide_reading)
        carbon_dioxide_mask = (carbon_dioxide_reading[:, bit]
                               != target_cO2[bit])
        carbon_dioxide_reading = carbon_dioxide_reading[carbon_dioxide_mask]

oxygen_reading = ''.join(oxygen_reading.flatten().astype(str))
oxygen_reading = int(oxygen_reading, base=2)

carbon_dioxide_reading = ''.join(carbon_dioxide_reading.flatten().astype(str))
carbon_dioxide_reading = int(carbon_dioxide_reading, base=2)

print(f'O2: {oxygen_reading}')
print(f'CO2: {carbon_dioxide_reading}')
print(f'O2*CO2: {oxygen_reading*carbon_dioxide_reading}')

