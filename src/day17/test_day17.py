from day17 import readTarget, bestInitialVx, bestInitialY, trajectory
from day17 import partOne, maximalInitialXY, findAllIV, partTwo


def test_readTarget():
    rangeX, rangeY = readTarget('target area: x=20..30, y=-10..-5')
    assert rangeX == [x for x in range(20, 31)]
    assert rangeY == [y for y in range(-10, -4)]

    rangeX, rangeY = readTarget('data/data_q17.txt')
    assert rangeX == [x for x in range(230, 284)]
    assert rangeY == [y for y in range(-107, -56)]


def test_bestInitialVx():
    rangeX, rangeY = readTarget('target area: x=20..30, y=-10..-5')
    vX0 = bestInitialVx(rangeX)
    assert vX0 == 6


def test_bestInitialY():
    rangeX, rangeY = readTarget('target area: x=20..30, y=-10..-5')
    vX0 = bestInitialY(rangeY)
    assert vX0 == 9


def test_trajectory():
    rangeX, rangeY = readTarget('target area: x=20..30, y=-10..-5')
    path = trajectory(9, 0, rangeX, rangeY)
    assert path[-1] == (30, -6)
    path = trajectory(17, -4, rangeX, rangeY)
    assert path is None


def test_partOne():
    assert partOne('target area: x=20..30, y=-10..-5') == 45


def test_maximalInitialXY():
    rangeX, rangeY = readTarget('target area: x=20..30, y=-10..-5')
    assert maximalInitialXY(rangeX, rangeY) == (30, -10)


def test_findAllIV():
    rangeX, rangeY = readTarget('target area: x=20..30, y=-10..-5')
    allIV = findAllIV(rangeX, rangeY)
    assert len(allIV) == 112


def test_partTwo():
    assert partTwo('target area: x=20..30, y=-10..-5') == 112
