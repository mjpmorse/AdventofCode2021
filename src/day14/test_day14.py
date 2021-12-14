from day14 import readTemplate, polymerization
from day14 import countOccurrences, partOne, partTwo


def test_readTemplate():
    template, polyDict = readTemplate('data/data_q14_dummy.txt')
    assert template == 'NNCB'
    assert len(polyDict.keys()) == 16
    assert polyDict['HN'] == 'C'


def test_polymerization():
    template, polyDict = readTemplate('data/data_q14_dummy.txt')

    polymer = polymerization(template, polyDict)
    assert polymer == 'NCNBCHB'

    polymer = polymerization(polymer, polyDict)
    assert polymer == 'NBCCNBBBCBHCB'


def test_countOccurrences():
    template, polyDict = readTemplate('data/data_q14_dummy.txt')
    polymer = polymerization(template, polyDict)
    occurrences = countOccurrences(polymer)
    assert len(occurrences.keys()) == 4
    assert occurrences['N'] == 2
    assert occurrences['C'] == 2
    assert occurrences['B'] == 2


def test_partOne():
    diff = partOne('data/data_q14_dummy.txt')
    assert diff == 1588


def test_partTwo():
    diff = partTwo('data/data_q14_dummy.txt')
    assert diff == 2188189693529