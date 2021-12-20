from typing import List, Tuple
import numpy as np
from io import StringIO
import copy
from icecream import ic

# TODO: CLEAN THIS! WRITE TESTS!
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
        self.distBTBeaconDict = {}
        for beacon in self.beacons:
            beacon.D2otherBeacons = np.array([[]])
        for pos1, beacon1 in enumerate(self.beacons):
            for pos2, beacon2 in enumerate(self.beacons[pos1 + 1:]):
                distance = beacon2 - beacon1
                beacon1.otherBeacon(beacon2)
                beacon2.otherBeacon(beacon1)
                distance = distance ** 2
                distance = np.sum(distance)
                distance = int(distance)
                self.distBTBeacons = np.append(
                    self.distBTBeacons,
                    distance
                )
                if distance not in self.distBTBeaconDict.keys():
                    self.distBTBeaconDict[distance] = []
                self.distBTBeaconDict[distance].append(
                    (beacon2.position, beacon1.position)
                )

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
                if len(line) != 3:
                    raise Exception('hfdjahkjl')
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


def scannerOverLap(scanner1: Scanner, scanner2: Scanner):
    local = 0
    scanner1.calculateDistBTBeacons()
    scanner2.calculateDistBTBeacons()
    for dist in scanner1.distBTBeacons:
        if dist in scanner2.distBTBeacons:
            local += 1
    if local >= 66:
        numBeacons = len(scanner2.beacons) - 12
        # print(f'scanners {scanner1} {scanner2} have {local} edges the same')
        return True, numBeacons

    return False, 0

def beaconOverlap(scanner1: Scanner, scanner2: Scanner) -> List:

    scanner1.calculateDistBTBeacons()
    scanner2.calculateDistBTBeacons()
    offshiftDict = {}

    for dist1, beacons1 in scanner1.distBTBeaconDict.items():
        for dist2, beacons2 in scanner2.distBTBeaconDict.items():

            if dist1 != dist2:
                continue
            for beacon1 in beacons1:
                for beacon2 in beacons2:
                    b11 = beacon1[0]
                    b12 = beacon1[1]
                    b21 = beacon2[0]
                    b22 = beacon2[1]
                    if np.array_equiv(b12 - b22, b11 - b21):
                        offshift = b12 - b22
                        if str(offshift) not in offshiftDict.keys():
                            offshiftDict[str(offshift)] = [offshift, 1]
                        else:
                            already = offshiftDict[str(offshift)][1]
                            offshiftDict[str(offshift)] = [offshift, already + 1]
    offset = None
    highest = 0
    # for key, value in offshiftDict.items():
    #     # ic(f'{key}: {value[1]}')
    #     if value[1] >= 12:
    #         highest = value[1]
    #         offset = value[0]

    if offshiftDict and len(offshiftDict.keys()) == 1:
        for offset1 in offshiftDict.values():
            if offset1[1] > 12:
                offset = offset1[0]
 
    return offset 


def allign_scanners(scannerList: List[Scanner]):
    scanner0__ = copy.deepcopy(scannerList[0])
    scannerList.pop(0)
    foundScanList = [scanner0__]
    i = 0
    nBeacons = len(scanner0__.beacons)

    while len(scannerList) > 0:
        # print(f'scanner 0 sees {len(scanner0_.beacons)} beacons')
        i += 1
        for scanner0 in foundScanList:
            # print(f'scanner {scanner0} being matched to')
            scanner0.calculateDistBTBeacons()
            for scanpos, scanner in enumerate(scannerList):
                noverlap, n = scannerOverLap(scanner0, scanner)
                if not noverlap:
                    continue
                updated = False
                # do the rotations
                for rotation in rotationList:
                    for beacon in scanner:
                        beacon.updatePosition(
                            np.matmul(rotation, beacon.originalPosition)
                            )
                    scanner.calculateDistBTBeacons()
                    offset = beaconOverlap(scanner0, scanner)
                    if offset is not None:
                        print(f'offset is {offset}')
                        # ic(f'{offset}, {scanner0.position}, {scanner.position}')
                        scanner.shiftLocation(offset)
                        foundScanList.append(scanner)
                        updated = True
                        nBeacons += n
                        break
                # if the scanner has been updated
                if updated:
                    # we will add beacons to the first
                    # for beacon in scanner:
                    #     if not any(np.array_equiv(beacon.position, x.position) for x in scanner0.beacons):
                    #         scanner0.addBeacon(beacon)
                    print(f'Scanner {scanner.name} is at {scanner.position[0]},{scanner.position[1]},{scanner.position[2]}')
                    # print(f'Scanner {scanner.name} matched to scanner0')
                    # print(f'Scanner 0 now sees {len(scanner0__.beacons)} beacons')
                    scannerList.pop(scanpos)
                    # print(f'{len(scannerList)} beacons left')
                    if len(scannerList) == 0:
                        break

        if i > 500:
            ic(f'{scannerList}')
            ic(f'{scanner0}')
            raise Exception('Too many iteration')
    print(f'{nBeacons} beacons found')
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
    scannerList = readInput('data/data_q19.txt')
    print(len(scannerList))
    aligned = allign_scanners(scannerList)
    known = countBeacons(aligned)
    print(len(known))

    distance = []
    for pos, scanner1 in enumerate(aligned):
        for scanner2 in aligned[pos + 1:]:
            d = scanner1.position - scanner2.position
            d = np.sum(np.abs(d))
            distance.append(d)

    print(distance)
    print(max(distance))

