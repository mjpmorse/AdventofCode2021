import numpy as np
from icecream import ic

with open('day02/data_q2.txt', 'r') as f:
    data = np.loadtxt(f, dtype=str)
    directions = data[:, 1].astype(int)
    command = data[:, 0]

if False:
    data = np.array([['forward', 5],
                     ['down', 5],
                     ['forward', 8],
                     ['up', 3],
                     ['down', 8],
                     ['forward', 2]])
    directions = data[:, 1].astype(int)
    command = data[:, 0]

aim = 0
depth = 0
position = 0

for command in data:
    if command[0] == 'down':
        aim += command[1].astype(int)

    elif command[0] == 'up':
        aim -= command[1].astype(int)

    elif command[0] == 'forward':
        position += command[1].astype(int)
        depth += aim * command[1].astype(int)

print(f"move down {depth} units and forward {position} units")
print(f"The product is {depth * position}")
