import numpy as np
from icecream import ic


def readData(file):
    with open(file, 'r') as f:
        data = np.loadtxt(f, dtype=str)
        directions = data[:, 1].astype(int)
        command = data[:, 0]
    return directions, command


def partOne(file):
    directions, command = readData(file)
    down = np.sum(directions[command == 'down']) - \
        np.sum(directions[command == 'up'])
    forward = np.sum(directions[command == 'forward'])
    return down * forward


def partTwo(file):
    aim = 0
    depth = 0
    position = 0

    with open(file, 'r') as f:
        for line in f:
            command = line.split(' ')
            if command[0] == 'down':
                aim += int(command[1])

            elif command[0] == 'up':
                aim -= int(command[1])

            elif command[0] == 'forward':
                position += int(command[1])
                depth += aim * int(command[1])

    return depth * position
