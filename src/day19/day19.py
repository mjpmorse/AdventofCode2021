from typing import List, Tuple
import numpy as np
from io import StringIO
import copy
from icecream import ic


class Beacon:
    def __init__(self, position: np.array):
        self.position = position
        self.originalPosition = copy.deepcopy(position)
        self.D2otherBeacons = np.array([[]])
        self.otherBeaconDict = {}

    def otherBeacon(self, __o: object):
        self.D2otherBeacons = np.append(
            self.D2otherBeacons,
            __o.position - self.position)
        self.D2otherBeacons = self.D2otherBeacons.reshape(-1, 3)    
        self.otherBeaconDict[str(__o.position)] = __o.position - self.position

    def __add__(self, __o: object) -> np.array:
        return self.position + __o.position

    def __sub__(self, __o: object) -> np.array:
        return self.position - __o.position

    def __repr__(self) -> str:
        return f'{self.position}'

    def updatePosition(self, position):
        self.position = position
        self.D2otherBeacons = np.array([])

    def __eq__(self, __o: object) -> bool:
        return self.position == __o.position


class Scanner:

    def __init__(self, name: str):
        self.name = name
        self.position = np.array([0, 0, 0])
        self.beacons = np.array([])
        self.distBTBeacons = np.array([])

    def addBeacon(self, beacon: Beacon):
        self.beacons = np.append(self.beacons, beacon)

    def calculateDistBTBeacons(self):
        for pos1, beacon1 in enumerate(self.beacons):
            for pos2, beacon2 in enumerate(self.beacons[pos1 + 1:]):
                distance = beacon2 - beacon1
                beacon1.otherBeacon(beacon2)
                beacon2.otherBeacon(beacon1)
                distance = distance ** 2
                distance = np.sum(distance)
                self.distBTBeacons = np.append(
                    self.distBTBeacons,
                    distance
                )

    def updatePosition(self, newPosition: np.array):
        self.position = newPosition
        for beacon in self.beacons:
            beacon.updatePosition(beacon.position + newPosition)
        self.calculateDistBTBeacons()

    def __repr__(self) -> str:
        return f'{self.beacons}'

    def __iter__(self) -> Beacon:
        for beacon in self.beacons:
            yield beacon


def readInput(file) -> List[Scanner]:
    scannerList = []
    with open(f'{file}', 'r') as f:
        for line in f:
            if '---' in line:
                line = line.replace(' ', '')
                line = line.split('---')[1]
                line = line.split('scanner')[1]
                scannerList.append(Scanner(line))
            if ',' in line:
                line = StringIO(line)
                line = np.loadtxt(line, dtype=int, delimiter=',')
                b = Beacon(line)
                scannerList[-1].addBeacon(b)
    return scannerList


id = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
ry = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
flipx = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
flipy = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
flipz = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])


rotationList = [
    id,
    rx, rx @ rx, rx @ rx @ rx,
    ry, ry @ ry, ry @ ry @ ry,
    rz, rz @ rz, rz @ rz @ rz,
]
for rotation in rotationList:
    if not any(np.array_equal(rx @ rotation, r) for r in rotationList):
        rotationList.append(rx @ rotation)
    if not any(np.array_equal(rx @ rx @ rotation, r) for r in rotationList):
        rotationList.append(rx @ rx @ rotation)
    if not any(np.array_equal(rx @ rx @ rx @ rotation, r) for r in rotationList):
        rotationList.append(rx @ rx @ rx @ rotation)
    if not any(np.array_equal(ry @ rotation, r) for r in rotationList):
        rotationList.append(ry @ rotation)
    if not any(np.array_equal(ry @ ry @ rotation, r) for r in rotationList):
        rotationList.append(ry @ ry @ rotation)
    if not any(np.array_equal(ry @ ry @ ry @ rotation, r) for r in rotationList):
        rotationList.append(ry @ ry @ ry @ rotation)
    if not any(np.array_equal(rz @ rotation, r) for r in rotationList):
        rotationList.append(rz @ rotation)
    if not any(np.array_equal(rz @ rz @ rotation, r) for r in rotationList):
        rotationList.append(rz @ rz @ rotation)
    if not any(np.array_equal(rz @ rz @ rz @ rotation, r) for r in rotationList):
        rotationList.append(rz @ rz @ rz @ rotation)


def allign_scanners(scannerList: List[Scanner]):
    scanner0 = scannerList[0]
    scannerList.pop(0)
    i = 0
    print(f'scanner 0 sees {len(scanner0.beacons)} beacons')
    while len(scannerList) > 0:
        i += 1
        for scanner in scannerList:
            updated = False
            scanner0.calculateDistBTBeacons()
            # do the rotations
            for rotation in rotationList:
                for beacon in scanner:
                    beacon.updatePosition(
                        np.matmul(rotation, beacon.originalPosition)
                        )
                scanner.calculateDistBTBeacons()
                inter = np.intersect1d(
                    scanner0.distBTBeacons,
                    scanner.distBTBeacons
                )
                if len(inter) >= 12:
                    for beacon0 in scanner0:
                        for beacon1 in scanner:
                            ic(f'{beacon0.D2otherBeacons}')
                            ic(f'{beacon1.D2otherBeacons}')
                            # TODO: fix this intersection 
                            interB = np.intersect1d(
                                beacon0.D2otherBeacons,
                                beacon1.D2otherBeacons, axis=1
                            )
                            ic(f'{interB}')
                            if len(interB) < 12:
                                continue
                            for x in interB:
                                print(x)
                            for value, key in beacon0.otherBeaconDict.items():
                                if any(np.array_equal(key, x) for x in interB):
                                    print(f'{value}: {key}')
                            for value, key in beacon.otherBeaconDict.items():
                                if any(np.array_equal(key, x) for x in interB):
                                    print(f'{value}: {key}')
                            scannerOffset = beacon0 - beacon1
                            scanner.updatePosition(scannerOffset)
                            updated = True
                            break
                        # if the scanner has been updated
                        if updated:
                            # we will add beacons to the first
                            beaconsScan0 = np.array(
                                [x.position for x in scanner0.beacons]
                                )
                            for beacon in scanner:
                                if beacon.position not in beaconsScan0:
                                    scanner0.addBeacon(beacon)
                            break
                if updated:
                    print(f'Scanner {scanner.name} is at {scanner.position[0]},{scanner.position[1]},{scanner.position[2]}')
                    print(f'Scanner {scanner.name} matched to scanner0')
                    print(f'Scanner 0 now sees {len(scanner0.beacons)} beacons')
                    scannerList.remove(scanner)
                    break
        if i > 500:
            ic(f'{scannerList}')
            ic(f'{scanner0}')
            raise Exception('Too many iteration')
    return scanner0, scannerList



if __name__ == '__main__':
    scannerList = readInput('../../data/data_q19_dummy.txt')
    scanner0, scannerlist = allign_scanners(scannerList)
    for beacon in scanner0:
        # print(f'{beacon.position[0]},{beacon.position[1]},{beacon.position[2]}')
        pass

