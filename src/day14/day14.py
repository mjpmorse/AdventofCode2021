from typing import Dict


def readTemplate(file):
    with open(file, 'r') as f:
        init = f.readline().strip()
        ends = (init[0], init[-1])
        initDict = {}
        polymerDict = {}
        f.readline()
        for line in f:
            line = line.strip()
            line = line.split(' -> ')
            polymerDict[line[0]] = line[1]
            initDict[line[0]] = 0
        for pos, letter in enumerate(init[:-1]):
            initDict[init[pos:pos + 2]] += 1

    return initDict, polymerDict, ends


def polymerization(polymer: Dict, insertion: Dict) -> Dict:
    newPolymer = {key: 0 for key in insertion.keys()}
    for pair, occur in polymer.items():
        toInsert = insertion[pair]
        leftPolymer = f'{pair[0]}{toInsert}'
        rightPolymer = f'{toInsert}{pair[1]}'
        newPolymer[leftPolymer] += occur
        newPolymer[rightPolymer] += occur

    return newPolymer


def countOccurrences(polymer: Dict, ends=()) -> Dict:
    allLetters = ''.join([x for x in polymer.keys()])
    uniqueLetters = set(allLetters)
    countDict = {lett: 0 for lett in uniqueLetters}

    for pair, count in polymer.items():
        firstLetter = pair[0]
        secondLetter = pair[1]
        countDict[firstLetter] += count
        countDict[secondLetter] += count
    for letter, count in countDict.items():
        if ends[0] == ends[1]:
            toRemove = 2
        else:
            toRemove = 1
        if letter in ends:
            countDict[letter] = (count - toRemove) // 2 + toRemove
        else:
            countDict[letter] = (count) // 2

    return countDict


def partOne(data, steps):
    polymer, polyDict, ends = readTemplate(data)

    for _ in range(steps):
        polymer = polymerization(polymer, polyDict)

    countDict = countOccurrences(polymer, ends)
    mostOften = 'B'
    leastOften = 'B'

    for monomer, count in countDict.items():
        if count > countDict[mostOften]:
            mostOften = monomer
        elif count < countDict[leastOften]:
            leastOften = monomer

    diff = countDict[mostOften] - countDict[leastOften]
    statement = (
        'The difference between the most  and least often '
        f'occurring monomer is ({mostOften}, {leastOften}) {diff}'
    )
    print(statement)
    return diff


if __name__ == '__main__':
    partOne('data/data_q14.txt', 10)
    partOne('data/data_q14.txt', 40)
