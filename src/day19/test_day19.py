from day19 import Scanner, Beacon, readInput, beaconOverlap


def test_readInput():
    scannerList = readInput('data/data_q19_dummy.txt')
    assert len(scannerList) == 5
    assert len(scannerList[0].beacons) == 25
    assert str(scannerList[3].beacons[4]) == '-458,-679,-417'


def test_beaconOverlap():
    scannerList = readInput('data/data_q19_dummy.txt')
    scanner0 = scannerList[0]
    scanner1 = scannerList[1]
    overlap = beaconOverlap(scanner0, scanner1)
    assert overlap == None
    

