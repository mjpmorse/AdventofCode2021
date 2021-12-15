from day15 import readCaveMap, calculateCost, increaseMapSize
from day15 import partOne, partTwo


def test_readCaveMap():
    caveMap = readCaveMap('data/data_q15_dummy.txt')
    assert len(caveMap) == 10
    assert len(caveMap[0]) == 10
    assert caveMap[0] == [1, 1, 6, 3, 7, 5, 1, 7, 4, 2]
    assert caveMap[-1] == [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]


def test_CaveGraph():
    caveMap = readCaveMap('data/data_q15_dummy.txt')
    lowerCorner = (len(caveMap) - 1, len(caveMap[-1]) - 1)
    cheapest = calculateCost(caveMap, (0, 0), lowerCorner)
    assert(len(cheapest[0]) == 19)
    assert cheapest[1] == 40


def test_partOne():
    assert partOne('data/data_q15_dummy.txt')[1] == 40


def test_increaseMapSize():
    caveMap = readCaveMap('data/data_q15_dummy.txt')
    newMap = increaseMapSize(caveMap, 5)
    assert len(newMap) == len(caveMap) * 5
    assert len(newMap[-1]) == len(caveMap[-1]) * 5
    assert newMap[0] == [
        1, 1, 6, 3, 7, 5, 1, 7, 4, 2,
        2, 2, 7, 4, 8, 6, 2, 8, 5, 3,
        3, 3, 8, 5, 9, 7, 3, 9, 6, 4,
        4, 4, 9, 6, 1, 8, 4, 1, 7, 5,
        5, 5, 1, 7, 2, 9, 5, 2, 8, 6]
    assert newMap[-1] == [
        6, 7, 5, 5, 4, 8, 8, 9, 3, 5,
        7, 8, 6, 6, 5, 9, 9, 1, 4, 6,
        8, 9, 7, 7, 6, 1, 1, 2, 5, 7,
        9, 1, 8, 8, 7, 2, 2, 3, 6, 8,
        1, 2, 9, 9, 8, 3, 3, 4, 7, 9]


def test_partTwo():
    assert partTwo('data/data_q15_dummy.txt')[1] == 315
