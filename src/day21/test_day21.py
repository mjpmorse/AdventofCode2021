from day21 import readData, partOne, DeterministicDie, partTwo, calcPos


def test_readData():
    assert readData('data/data_q21_dummy.txt') == [4, 8]


def test_DeterministicDie():
    die = DeterministicDie()
    assert die.roll3Times() == 6
    assert die.roll3Times() == 15
    assert die.roll3Times() == 24


def test_partOne():
    assert partOne('data/data_q21_dummy.txt') == 739785


def test_calcPos():
    assert calcPos(1, 1) == 2
    assert calcPos(10, 1) == 1
    assert calcPos(10, 2) == 2
    assert calcPos(10, 3) == 3
    assert calcPos(9, 3) == 2
    assert calcPos(9, 2) == 1
    assert calcPos(9, 1) == 10


def test_partTwo():
    assert partTwo('data/data_q21_dummy.txt') == 444356092776315
