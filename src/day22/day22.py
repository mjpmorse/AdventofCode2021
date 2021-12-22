'''
shout out to
https://stackoverflow.com/questions/5009526/overlapping-cubes
'''
from os import read
from typing import Dict, List, Tuple
import numpy as np
from icecream import ic


def readData(file: str) -> List[Tuple]:
    cmd = []
    with open(f'{file}', 'r') as f:
        for line in f:
            line = line.split('x=')
            cmd0 = line[0].strip()
            line = line[1].split(',y=')
            xcmd = line[0].split('..')
            xcmd = range(int(xcmd[0]), int(xcmd[1]) + 1)
            line = line[1].split(',z=')
            ycmd = line[0].split('..')
            ycmd = range(int(ycmd[0]), int(ycmd[1]) + 1)
            zcmd = line[1].split('..')
            zcmd = range(int(zcmd[0]), int(zcmd[1]) + 1)
            cmd.append((cmd0, xcmd, ycmd, zcmd))
    return cmd


def turnOnOff(cmdList: List) -> Dict:
    reactorDict = {}
    for n, cmd in enumerate(cmdList):
        print(f'on cmd {n}')
        for x in cmd[1]:
            if x not in reactorDict.keys():
                reactorDict[x] = {}
            for y in cmd[2]:
                if y not in reactorDict[x].keys():
                    reactorDict[x][y] = {}
                for z in cmd[3]:
                    if cmd[0] == 'on' and z not in reactorDict[x][y].keys():
                        reactorDict[x][y][z] = 1
                        continue
                    if cmd[0] == 'off' and z in reactorDict[x][y].keys():
                        reactorDict[x][y].pop(z)
    return reactorDict


def partOne(file):
    cmdList = readData(file)
    cmdList2 = []
    for cmd in cmdList:
        x = cmd[1]
        y = cmd[2]
        z = cmd[3]
        if x[0] < -50:
            x = range(-50, x[-1])
        if y[0] < -50:
            y = range(-50, y[-1])
        if z[0] < -50:
            z = range(-50, z[-1])
        if len(x) > 0 and x[-1] > 51:
            x = range(x[0], 51)
        if len(y) > 0 and y[-1] > 51:
            y = range(y[0], 51)
        if len(z) > 0 and z[-1] > 51:
            z = range(z[0], 51)
        condition = (
            len(x) > 0 and
            len(y) > 0 and
            len(z) > 0
        )
        if condition:
            cmdList2.append(
                (cmd[0], x, y, z))

    reactorDict = turnOnOff(cmdList2)
    onCount = 0
    for v1 in reactorDict.values():
        for v2 in v1.values():
            for v3 in v2.values():
                onCount += v3
    statement = (
        f'There are {onCount} reactors on'
    )
    print(statement)
    return onCount


def partTwo(file):
    cmdList = readData(file)
    reactorDict = turnOnOff(cmdList)
    onCount = 0
    for v1 in reactorDict.values():
        for v2 in v1.values():
            for v3 in v2.values():
                onCount += v3
    statement = (
        f'There are {onCount} reactors on'
    )
    print(statement)
    return onCount

class Cube:
    def __init__(self, mode,
                 x1, x2,
                 y1, y2,
                 z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.mode = mode


def cubeIntersectionAdd(cubeA: List, cubeB: List) -> List:
    # cube A is to the right of B
    con1 = cubeA.x2 < cubeB.x1
    # cube A is to the left of B
    con2 = cubeB.x2 < cubeA.x1
    # cube A is below B
    con3 = cubeA.z2 < cubeB.z1
    # cube A is above B
    con4 = cubeB.z2 < cubeA.z1
    # cube A is below B
    con5 = cubeA.y2 < cubeB.y1
    # cube A is in-front of B
    con5 = cubeB.y2 < cubeA.y1

    # an overlap is happens if any of these are false
    # if we have an overlap we want ot break the cubes down into 
    # non overlaping cubes:


















if __name__ == '__main__':
    partOne('data/q22.txt')
    partTwo('data/q22_dummy.txt')
