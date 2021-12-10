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
gamma = np.floor(2 * np.sum(data, axis=0))/len(data)
gamma = gamma.astype(int).astype(str)
gamma = int(''.join(gamma), base=2)
# bit flip gamma to get epsilon
num_digits = data.shape[1]
base_2 = f"0b{'1' * num_digits}"

epsilon = gamma ^ int(base_2, base=2)


print(f'gamma: {gamma}, epsilon: {epsilon}, epsilon*gamma: {epsilon*gamma}')
