from day02 import readData, partOne, partTwo


def test_readData():
    directions, command = readData('data/data_q2.txt')
    assert len(directions) == len(command)


def test_partOne():
    assert partOne('data/data_q2.txt') == 1989014


def test_partTwo():
    assert partTwo('data/data_q2.txt') == 2006917119