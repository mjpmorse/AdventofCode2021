from day22 import readData, partOne, partTwo


def test_readData():
    cmd = readData('data/q22.txt')
    assert len(cmd) == 420
    assert len(cmd[0]) == 4
    assert cmd[0][0] == 'on'
    assert cmd[0][1] == range(-31, 17 + 1)
    assert cmd[0][2] == range(-17, 30 + 1)
    assert cmd[0][3] == range(-43, 8 + 1)
    assert cmd[-1][1] == range(-47814, -25131 + 1)
    assert cmd[-1][2] == range(46029, 74913 + 1)
    assert cmd[-1][3] == range(36938, 62900 + 1)


def test_partOne():
    assert partOne('data/q22_dummy.txt') == 590784
    assert partOne('data/q22.txt') == 533863

