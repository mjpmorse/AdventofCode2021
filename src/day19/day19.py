from typing import List, Tuple
import numpy as np
from io import StringIO
import copy
from icecream import ic


class Beacon:
    def __init__(self, position: np.array):
        self.position = position
        self.originalPosition = position
        self.D2otherBeacons = np.array([[]])
        self.otherBeaconDict = {}

    def otherBeacon(self, __o: object):
        diff = __o.position - self.position
        self.D2otherBeacons = np.append(
          self.D2otherBeacons,
          diff
        )
        self.D2otherBeacons = self.D2otherBeacons.reshape(-1, 3)
        id_str = f'{diff[0]},{diff[1]},{diff[2]}'

        self.otherBeaconDict[id_str] = diff

    def __add__(self, __o: object) -> np.array:
        return self.position + __o.position

    def __sub__(self, __o: object) -> np.array:
        return self.position - __o.position

    def __repr__(self) -> str:
        return f'{self.position[0]},{self.position[1]},{self.position[2]}'

    def updatePosition(self, position):
        self.position = position
        self.D2otherBeacons = np.array([[]])

    def __eq__(self, __o: object) -> bool:
        return self.position == __o.position


class Scanner:

    def __init__(self, name: str):
        self.name = name
        self.position = np.array([0, 0, 0])
        self.beacons = np.array([])
        self.distBTBeacons = np.array([])
        self.distBTBeaconDict = {}

    def addBeacon(self, beacon: Beacon):
        self.beacons = np.append(self.beacons, beacon)

    def __lt__(self, __o: object):
        return len(self.beacons) < len(__o.beacons)

    def calculateDistBTBeacons(self):
        self.distBTBeacons = np.array([])
        for beacon in self.beacons:
            beacon.D2otherBeacons = np.array([[]])
        for pos1, beacon1 in enumerate(self.beacons):
            for pos2, beacon2 in enumerate(self.beacons[pos1 + 1:]):
                scannerList = beacon2 - beacon1
                beacon1.otherBeacon(beacon2)
                beacon2.otherBeacon(beacon1)
                distance = distance ** 2
                distance = np.sum(distance)
                self.distBTBeacons = np.append(
                    self.distBTBeacons,
                    distance
                )
                if distance not in self.distBTBeacons.keys

    def shiftLocation(self, newPosition: np.array):
        self.position = newPosition
        for beacon in self.beacons:
            beacon.updatePosition(beacon.position + newPosition)
        self.calculateDistBTBeacons()

    def __repr__(self) -> str:
        return f'{self.name}'

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
flip = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])

rotationList = [
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
    np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]),
    # neg x
    np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
    np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]]),
    np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
    np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]]),
    # y
    np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),
    np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]]),
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
    # neg y
    np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]),
    np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
    np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]),
    np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]),
    # z
    np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
    np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]),
    np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
    np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),
    # -z
    np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]]),
    np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
    np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]]),
    np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]]),
]

def scannerOverLap(scannerList):
    overlap = []

    for pos, scanner0 in enumerate(scannerList):
        scanner0.calculateDistBTBeacons()
        for scanner1 in scannerList[pos + 1:]:
            scanner1.calculateDistBTBeacons()
            local = 0
            for dist in scanner0.distBTBeacons:
                if dist in scanner1.distBTBeacons:
                    local += 1
            if local >= 66:
                overlap.append((scanner0, scanner1))

    return overlap



def beaconOverlap(scanner1: Scanner, scanner2: Scanner) -> List:

    scanner1.calculateDistBTBeacons()
    scanner2.calculateDistBTBeacons()
    numOverlaps = 0
    for dis in scanner1.distBTBeacons:
        if dis in scanner2.distBTBeacons:
            numOverlaps += 1

    # a fully connected 12 node graph has 66 edges
    # ic(numOverlaps)
    if numOverlaps < 66:
        return None

    for nb1, b11 in enumerate(scanner1.beacons):
        for b12 in scanner1.beacons[nb1 + 1:]:
            d1 = np.sum((b11 - b12)**2)
            d1c = np.count_nonzero(scanner1.distBTBeacons == d1)
            for nb2, b21 in enumerate(scanner2.beacons):
                for b22 in scanner2.beacons[nb2 + 1:]:
                    d2 = np.sum((b21 - b22)**2)
                    d2c = np.count_nonzero(scanner2.distBTBeacons == d2)
                    # if d2c != 1 and d1c != 1:
                    #     continue
                    # ic(d2c)
                    if not np.array_equiv(d1, d2):
                        continue

                    if np.array_equiv(b12 - b22, b11 - b21):
                        offshift = b12 - b22
                        print(f'found it: {offshift} {b11 - b21}')
                        # ic(f'{b11}, {b12}, {b21}, {b22}')
                        return offshift
                    else:
                        # ic(f'didnt find it; {b12 - b22} {b11 - b21}')
                        # ic(f'{b11}, {b12}, {b21}, {b22}')
                        return None
    return None


def allign_scanners(scannerList: List[Scanner]):
    overlaps = scannerOverLap(scannerList)
    ic(f'{overlaps}')
    scanner0__ = copy.deepcopy(scannerList[0])
    scannerList.pop(0)
    foundScanList = [scanner0__]
    i = 0

    while len(scannerList) > 0:
        # print(f'scanner 0 sees {len(scanner0_.beacons)} beacons')
        i += 1
        for scanner0 in foundScanList:
            print(f'scanner {scanner0} being matched to')
            for scanpos, scanner in enumerate(scannerList):
                if (scanner0, scanner) not in overlaps and (scanner, scanner0) not in overlaps:
                    continue
                updated = False
                # do the rotations
                for rotation in rotationList:
                    for beacon in scanner:
                        beacon.updatePosition(
                            np.matmul(rotation, beacon.originalPosition)
                            )
                    scanner.calculateDistBTBeacons()
                    scanner0.calculateDistBTBeacons()
                    offset = beaconOverlap(scanner0, scanner)
                    if offset is not None:
                        print(f'offset is {offset}')
                        scanner.shiftLocation(scanner.position + offset)
                        foundScanList.append(scanner)
                        updated = True
                        break
                # if the scanner has been updated
                if updated:
                    # we will add beacons to the first
                    # for beacon in scanner:
                    #     if beacon.position not in scanner0__.beacons:
                    #         scanner0__.addBeacon(beacon)
                    print(f'Scanner {scanner.name} is at {scanner.position[0]},{scanner.position[1]},{scanner.position[2]}')
                    print(f'Scanner {scanner.name} matched to scanner0')
                    print(f'Scanner 0 now sees {len(scanner0__.beacons)} beacons')
                    scannerList.pop(scanpos)
                    print(f'{len(scannerList)} beacons left')
                    # break

        if i > 500:
            ic(f'{scannerList}')
            ic(f'{scanner0}')
            raise Exception('Too many iteration')
    return foundScanList


def countBeacons(scannerList: List[Scanner]) -> int:

    knownBeacons = []
    knownBeaconsStr = set()
    for scanner in scannerList:
        for beacon in scanner.beacons:
            knownBeaconsStr.add(str(beacon))
    return knownBeaconsStr



from time import sleep
if __name__ == '__main__':
    scannerList = readInput('data/data_q19_dummy.txt')
    aligned = allign_scanners(scannerList)
    known = countBeacons(aligned)
    print(len(known))

