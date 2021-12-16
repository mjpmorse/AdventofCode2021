def readPacket(file):
    try:
        packet = ''
        with open(f'{file}', 'r') as f:
            for line in f:
                line =\
                    [bin(int(x, 16))[2:].rjust(4, '0') for x in line.strip()]
                line = ''.join(line)
                packet += line
    except FileNotFoundError:
        packet = ''
        line = [bin(int(x, 16))[2:].rjust(4, '0') for x in file.strip()]
        line = ''.join(line)
        packet += line

    return packet


def readVersion(packet):
    fistThree = ''.join(packet[:3])
    return int(fistThree, 2)


def readType(packet):
    typeThree = ''.join(packet[3:6])
    return int(typeThree, 2)


def parseLiteral(packet):
    literal = ''
    for pos in range(6, len(packet), 5):
        literal += ''.join(packet[pos + 1: pos + 5])
        if int(packet[pos], 2) == 0:
            break
    lastposition = pos + 5
    return (int(literal, 2), lastposition)


def parsePacket(packet):
    packetType = readType(packet)
    packetVersion = readVersion(packet)
    packetLen = len(packet)
    '''
    If packet version ID is 4, we have
    a literal. A literal is of length
    n where 4 | n. Being brocken in to 5
    byte blocks.
    '''
    content = []
    returnTuple = (packetVersion, packetType, content)
    if packetType == 4:
        literal, lastPos = parseLiteral(packet)
        # if packet is version 4, can not have a subpacket
        # but we can have a large remainder because of
        # multiple literals in a row being parsed.
        # always need VVV TTT xxxx for any packet
        returnTuple = (packetVersion, packetType, literal)
        if packetLen - lastPos > 8:
            pass
        return returnTuple, lastPos

    else:
        bitLabel = int(packet[6], 2)
        if bitLabel == 0:
            # here we know length of total substring
            # associated with our operator
            length = packet[7: 7 + 15]
            length = int(length, 2)
            # remainder here will always be less than 8
            remainder = length
            lastPos = 22
            while remainder > 8:
                subpackage, next = parsePacket(packet[lastPos: 22 + length])
                lastPos += next
                remainder = 22 + length - lastPos
                content.append(subpackage)
        else:
            # TODO: while in the number of subpackets, reparse with remainder
            # after that reparse what is left not connected to the operator
            numberOfSubPackets = packet[7: 7 + 11]
            numberOfSubPackets = int(numberOfSubPackets, 2)
            lastPos = 7 + 11
            for _ in range(numberOfSubPackets):
                subpackage, next = parsePacket(packet[lastPos:])
                lastPos = lastPos + next
                content.append(subpackage)

        return returnTuple, lastPos


def sumVersionNumbers(output):
    versionTotal = 0
    versionTotal += output[0]
    if isinstance(output[2], int):
        itt = [output[2]]
    else:
        itt = output[2]
    for sub in itt:
        if isinstance(sub, tuple):
            versionTotal += sumVersionNumbers(sub)
    return versionTotal


def applyRulesRecursive(output):
    for sub in output[2]:
        if isinstance(sub, tuple):
            sub = applyRulesRecursive(sub)
        return applyRule(sub)


def applyRule(output):
    idType = output[1]
    subPacket = output[2]
    if idType == 0:
        result = 0
        for packet in subPacket:
            if isinstance(packet[2], list):
                packet = applyRule(packet)
                result += packet
            else:
                result += packet[2]

    elif idType == 1:
        result = 1
        for packet in subPacket:
            if isinstance(packet[2], list):
                packet = applyRule(packet)
                result *= packet
            else:
                result *= packet[2]

    elif idType == 2:
        tmpList = []
        for packet in subPacket:
            if isinstance(packet[2], list):
                packet = applyRule(packet)
                tmpList.append(packet)
            else:
                tmpList.append(packet[2])
        result = min(tmpList)

    elif idType == 3:
        tmpList = []
        for packet in subPacket:
            if isinstance(packet[2], list):
                packet = applyRule(packet)
                tmpList.append(packet)
            else:
                tmpList.append(packet[2])
        result = max(tmpList)

    elif idType == 5:
        tmplist = []
        for packet in subPacket:
            if isinstance(packet[2], list):
                tmplist.append(applyRule(packet))
            else:
                tmplist.append(packet[2])
        first = tmplist[0]
        second = tmplist[1]
        result = int(first > second)

    elif idType == 6:
        tmplist = []
        for packet in subPacket:
            if isinstance(packet[2], list):
                tmplist.append(applyRule(packet))
            else:
                tmplist.append(packet[2])
        first = tmplist[0]
        second = tmplist[1]
        result = int(first < second)

    elif idType == 7:
        tmplist = []
        for packet in subPacket:
            if isinstance(packet[2], list):
                tmplist.append(applyRule(packet))
            else:
                tmplist.append(packet[2])
        first = tmplist[0]
        second = tmplist[1]
        result = int(first == second)

    return result


def partOne(data):
    packet = readPacket(data)
    result = parsePacket(packet)
    total = sumVersionNumbers(result[0])
    statement = (
        f'The total of the version numbers is {total}'
    )
    print(statement)
    return total


def partTwo(data):
    packet = readPacket(data)
    result = parsePacket(packet)
    result = result[0]
    result = applyRule(result)

    statement = (
        f'The answer is {result}'
    )
    print(statement)
    return result


if __name__ == '__main__':
    partOne('data/data_q16.txt')
    partTwo('data/data_q16.txt')