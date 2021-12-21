from day01 import readData, partOne, partTwo


def test_readData():
    data = readData('data/data_q1.txt')
    assert len(data) == 2000


def test_partOne():
    length = partOne('data/data_q1.txt')
    assert length == 1167


def test_partTwo():
    length = partTwo('data/data_q1.txt')
    assert length == 1130
