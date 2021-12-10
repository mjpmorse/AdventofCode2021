import numpy as np
from icecream import ic

with open('data/data_q2.txt', 'r') as f:
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

down = np.sum(directions[command == 'down']) - \
       np.sum(directions[command == 'up'])
forward = np.sum(directions[command == 'forward'])

print(f"move down {down} units and forward {forward} units")
print(f"The product is {down * forward}")
