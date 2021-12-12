from day12 import findPaths, readCaveConnections
from day12 import partOne, partTwo


def test_readCaveConnections():

    caveConnections = readCaveConnections(
        'data/data_q12_dummy.txt'
    )

    assert len(caveConnections) == 7
    assert caveConnections[0] == ('start', 'A')
    assert caveConnections[-1] == ('b', 'end')


caveConnections = readCaveConnections(
        'data/data_q12_dummy.txt'
    )


def test_findPaths():
    paths = findPaths(caveConnections)
    assert len(paths) == 10


def test_partOne():
    allPaths = partOne()
    len(allPaths) == 4707


def test_partTwo():
    paths = partTwo('data/data_q12_dummy.txt')
    assert len(paths) == 36
