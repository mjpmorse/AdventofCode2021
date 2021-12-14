from icecream import ic

debug = True

def readTemplate(file):
    with open(file, 'r') as f:
        initialTemplate = f.readline().strip()
        polymerDict = {}
        f.readline()
        for line in f:
            line = line.strip()
            line = line.split(' -> ')
            polymerDict[line[0]] = line[1]
    return initialTemplate, polymerDict


def polymerization(polymer, insertion):
    newPolymer = polymer[0]
    for pos, letter in enumerate(polymer[:-1]):
        monomerToAdd = insertion[polymer[pos:pos + 2]]
        toAdd = f'{monomerToAdd}{polymer[pos+1]}'
        newPolymer = newPolymer + toAdd
    return newPolymer


def countOccurrences(polymer):
    countDict = {}
    uniqueLetters = set(polymer)
    for letter in uniqueLetters:
        countDict[letter] = polymer.count(letter)
    return countDict


def partOne(data):
    polymer, polyDict = readTemplate(data)

    for _ in range(10):
        polymer = polymerization(polymer, polyDict)

    occurrences = countOccurrences(polymer)
    mostOften = ['', 0]
    leastOften = ['', len(polymer)]
    for monomer, count in occurrences.items():
        if count > mostOften[1]:
            mostOften[1] = count
            mostOften[0] = monomer
        elif count < leastOften[1]:
            leastOften[1] = count
            leastOften[0] = monomer

    diff = mostOften[1] - leastOften[1]
    statement = (
        'The difference between the most  and least often '
        f'occurring monomer is ({mostOften[0]}, {leastOften[0]}) {diff}'
    )
    print(statement)
    return diff


def partTwo(data):
    polymer, polyDict = readTemplate(data)

    for _ in range(40):
        polymer = polymerization(polymer, polyDict)

    occurrences = countOccurrences(polymer)
    mostOften = ['', 0]
    leastOften = ['', len(polymer)]
    for monomer, count in occurrences.items():
        if count > mostOften[1]:
            mostOften[1] = count
            mostOften[0] = monomer
        elif count < leastOften[1]:
            leastOften[1] = count
            leastOften[0] = monomer

    diff = mostOften[1] - leastOften[1]
    statement = (
        'The difference between the most  and least often '
        f'occurring monomer is ({mostOften[0]}, {leastOften[0]}) {diff}'
    )
    print(statement)
    return diff


partOne('data/data_q14.txt')
