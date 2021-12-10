from icecream import ic

debug = False
inputValues = []
outputValues = []

with open('data/data_q8.txt', 'r') as f:
    for line in f:
        line = line.split(' | ')
        tmpI = [x.strip() for x in line[0].split(' ')]
        tmpO = [x.strip() for x in line[1].split(' ')]
        inputValues.append(tmpI)
        outputValues.append(tmpO)


def locationFinder(input):
    locationDict = {
        "top": '',
        "bottom": '',
        "middle": '',
        "leftTop": '',
        "leftBottom": '',
        "rightTop": '',
        "rightBottom": ''
    }

    ic(input) if debug else ""
    unknownLen5 = []
    unknownLen6 = []
    for signal in input:
        signal = set(signal)
        signalLen = len(signal)
        if signalLen == 2:
            one = signal
        elif signalLen == 3:
            seven = signal
        elif signalLen == 4:
            four = signal
        elif signalLen == 5:
            unknownLen5.append(signal)
        elif signalLen == 6:
            unknownLen6.append(signal)
        elif signalLen == 7:
            eight = signal
        else:
            raise ValueError

    '''
    1 and 7 can be used to determine the top,
    top is in 7 but not one.
    '''

    locationDict['top'] = set(seven).difference(set(one)).pop()
    ic(f"top: {set(seven).difference(set(one)).pop()}") if debug else ""

    '''
    1 and 6 can be used to determine the lower right,
    6 is the only 6 unknown which shares one segment with
    one. Upper right is what is left of one.
    '''

    for unknown in unknownLen6:
        sharedWithOne = unknown.intersection(one)
        if len(sharedWithOne) == 1:
            locationDict['rightTop'] = one.difference(sharedWithOne).pop()
            ic(f"rightTop: {locationDict['rightTop']}") if debug else ""
            locationDict['rightBottom'] = sharedWithOne.pop()
            ic(f"rightBottom: {locationDict['rightBottom']}") if debug else ""
            unknownLen6.remove(unknown)
            break

    '''
    3 and 4 can give us the middle and upper left and bottom
    '''
    for unknown in unknownLen5:
        for value in locationDict.values():
            if value in unknown:
                unknown.remove(value)
            if value in four:
                four.remove(value)
        sharedWithFour = unknown.intersection(four)
        # 3 will be only len(5) with 2 unknown and 1 shared with 4
        if len(sharedWithFour) == 1 and len(unknown) == 2:
            locationDict['middle'] = set(sharedWithFour).pop()
            ic(f"middle: {locationDict['middle']}") if debug else ""

            locationDict['leftTop'] = four.difference(sharedWithFour).pop()
            ic(f"leftTop: {locationDict['leftTop']}") if debug else ""

            locationDict['bottom'] =\
                unknown.difference(sharedWithFour).pop()
            ic(f"unknown: {unknown}") if debug else ""
            ic(f"four: {four}") if debug else ""
            ic(f"sharedWithFour: {sharedWithFour}") if debug else ""
            ic(f"diff: {unknown.difference(four)}") if debug else ""
            ic(f"bottom: {locationDict['bottom']}") if debug else ""

            unknownLen5.remove(unknown)
            break

    '''
    Only thing that is left is the left bottom. Bottom
    Will be what ever letter in eight is not already a value
    '''
    for value in locationDict.values():
        if value in eight:
            eight.remove(value)

    if len(eight) == 1:
        locationDict['leftBottom'] = eight.pop()
        ic(locationDict) if debug else ""
        return locationDict
    else:
        ic(locationDict)
        ic(eight)
        raise Exception("There is a bug mate.")


def makeNumbers(outputList, locationDict):
    outputNumbers = []
    # it might be easier to invert the dictionary
    # keys here are letters, values are positions
    locationDictInvert = {v: k for k, v in locationDict.items()}
    keySet = set(locationDict.keys())
    numbers = {
        frozenset(keySet - set(['middle'])): '0',
        frozenset(['rightTop', 'rightBottom']): '1',
        frozenset(keySet - set(['leftTop', 'rightBottom'])): '2',
        frozenset(keySet - set(['leftTop', 'leftBottom'])): '3',
        frozenset(['leftTop', 'rightTop', 'middle', 'rightBottom']): '4',
        frozenset(keySet - set(['rightTop', 'leftBottom'])): '5',
        frozenset(keySet - set(['rightTop'])): '6',
        frozenset(['rightTop', 'rightBottom', 'top']): '7',
        frozenset(keySet): '8',
        frozenset(keySet - set(['leftBottom'])): '9'
    }
    ic(numbers) if debug else ""
    for output in outputList:
        tmp = set()
        for letter in output:
            ic(f"output: {output}, letter: {letter}") if debug else ""
            tmp.add(locationDictInvert[letter])
            ic(f"tmp is {tmp}") if debug else ""
        outputNumbers.append(numbers[frozenset(tmp)])
        outputNumber = "".join(outputNumbers)
    ic(f"numbers are is {outputNumbers}, {outputNumber}") if debug else ""
    return (outputNumbers, outputNumber)


totalValue = 0
for line in range(len(outputValues)):
    locationDict = locationFinder(inputValues[line])
    valueList, value = makeNumbers(outputValues[line], locationDict)
    totalValue += int(value)

print(f'The sum of the outputs is {totalValue}')
