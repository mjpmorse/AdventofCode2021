from day14 import readTemplate, polymerization, countOccurrences
from day14 import partOne


def test_readTemplate():
    initDict, polyDict, ends = readTemplate('data/data_q14_dummy.txt')
    assert len(polyDict.keys()) == 16
    assert polyDict['HN'] == 'C'
    assert len(initDict.keys()) == 16
    assert ends[0] == 'N'
    assert ends[1] == 'B'

    for key, value in initDict.items():
        if key not in ['NC', 'NN', 'CB']:
            assert value == 0
        else:
            assert value == 1


def test_polymerization():
    template, polyDict, ends = readTemplate('data/data_q14_dummy.txt')

    polymer = polymerization(template, polyDict)
    for key, value in polymer.items():
        if key not in ['NC', 'CN', 'NB', 'CH', 'HB', 'BC']:
            assert value == 0
        else:
            assert value == 1

def test_countOccurrences():
    template, polyDict, ends = readTemplate('data/data_q14_dummy.txt')
    polymer = polymerization(template, polyDict)
    occurrences = countOccurrences(polymer, ends)
    assert len(occurrences.keys()) == 4
    assert occurrences['N'] == 2
    assert occurrences['C'] == 2
    assert occurrences['B'] == 2


def test_partOne():
    diff = partOne('data/data_q14_dummy.txt', 10)
    assert diff == 1588


def test_partTwo():
    diff = partOne('data/data_q14_dummy.txt', 40)
    assert diff == 2188189693529