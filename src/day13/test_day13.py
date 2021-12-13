from day13 import readInstructions, makeDotMatrix
from day13 import foldDotMatrix, partOne, partTwo


def test_readInstructions():
    dotLocation, instructions = readInstructions('data/data_q13_dummy.txt')
    assert len(instructions) == 2
    assert instructions[0] == (0, 7)
    assert len(dotLocation) == 18
    assert dotLocation[0] == (6, 10)
    assert dotLocation[-1] == (9, 0)


def test_makeDotMatrix():
    dotLocation, instructions = readInstructions('data/data_q13_dummy.txt')
    dotMatrix = makeDotMatrix(dotLocation)
    assert len(dotMatrix) == 15
    assert len(dotMatrix[0]) == 11
    assert dotMatrix[0] == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert dotMatrix[1] == [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    assert dotMatrix[2] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert dotMatrix[-1] == [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]


def test_foldDotMatrix():
    dotLocation, instructions = readInstructions('data/data_q13_dummy.txt')
    dotMatrix = makeDotMatrix(dotLocation)
    dotMatrix = foldDotMatrix(dotMatrix, instructions[0])
    assert len(dotMatrix) == 7
    assert len(dotMatrix[0]) == 11
    assert dotMatrix[0][3] == 1
    assert dotMatrix[1][4] == 1
    assert dotMatrix[-1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # changes
    assert dotMatrix[0][2] == 1
    assert dotMatrix[0][0] == 1

    dotMatrix = foldDotMatrix(dotMatrix, instructions[1])
    assert len(dotMatrix) == 7
    assert len(dotMatrix[0]) == 5
    assert dotMatrix[-1] == [0, 0, 0, 0, 0]
    assert dotMatrix[-2] == [0, 0, 0, 0, 0]
    assert dotMatrix[-3] == [1, 1, 1, 1, 1]
    assert dotMatrix[-4] == [1, 0, 0, 0, 1]
    assert dotMatrix[0] == [1, 1, 1, 1, 1]


def test_partOne():
    assert partOne('data/data_q13_dummy.txt') == 17


def test_partTwo():
    dotMatrix = partTwo('data/data_q13_dummy.txt')
    assert len(dotMatrix) == 7
    assert len(dotMatrix[0]) == 5
    assert dotMatrix[0] == [1, 1, 1, 1, 1]
    assert dotMatrix[1] == [1, 0, 0, 0, 1]
    assert dotMatrix[2] == [1, 0, 0, 0, 1]
    assert dotMatrix[3] == [1, 0, 0, 0, 1]
    assert dotMatrix[4] == [1, 1, 1, 1, 1]
    assert dotMatrix[5] == [0, 0, 0, 0, 0]
    assert dotMatrix[6] == [0, 0, 0, 0, 0]
