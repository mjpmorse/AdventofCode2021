from day16 import readPacket, readType, readVersion
from day16 import parseLiteral, parsePacket, sumVersionNumbers
from day16 import partOne, applyRule, partTwo


def test_readPacket():
    packet = readPacket('data/data_q16_dummy.txt')
    packetStr = ''.join(x for x in packet)
    assert packetStr == '110100101111111000101000'


def test_readVersion():
    packet = readPacket('data/data_q16_dummy.txt')
    packetVersion = readVersion(packet)
    assert packetVersion == 6

    packet = readPacket('A0016C880162017C3686B18A3D4780')
    packetVersion = readVersion(packet)
    assert packetVersion == 5


def test_readType():
    packet = readPacket('data/data_q16_dummy.txt')
    packetType = readType(packet)
    assert packetType == 4

    packet = readPacket('A0016C880162017C3686B18A3D4780')


def test_parseLiteral():
    packet = readPacket('D2FE28')
    result = parseLiteral(packet)
    assert result == (2021, len(packet) - 3)


def test_parsePacket():
    packet = readPacket('38006F45291200')
    result = parsePacket(packet)
    assert result[0] == (1, 6, [(6, 4, 10), (2, 4, 20)])

    packet = readPacket('EE00D40C823060')
    result = parsePacket(packet)
    assert result[0] == (7, 3, [(2, 4, 1), (4, 4, 2), (1, 4, 3)])


def test_sumVersionNumbers():
    packet = readPacket('8A004A801A8002F478')
    result = parsePacket(packet)
    assert sumVersionNumbers(result[0]) == 16

    packet = readPacket('620080001611562C8802118E34')
    result = parsePacket(packet)
    assert sumVersionNumbers(result[0]) == 12

    packet = readPacket('C0015000016115A2E0802F182340')
    result = parsePacket(packet)
    assert sumVersionNumbers(result[0]) == 23

    packet = readPacket('A0016C880162017C3686B18A3D4780')
    result = parsePacket(packet)
    assert sumVersionNumbers(result[0]) == 31


def test_partOne():
    result = partOne('8A004A801A8002F478')
    assert result == 16


def test_applyRule():
    packet = readPacket('C200B40A82')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 3

    packet = readPacket('04005AC33890')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 54

    packet = readPacket('880086C3E88112')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 7

    packet = readPacket('CE00C43D881120')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 9

    packet = readPacket('D8005AC2A8F0')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 1

    packet = readPacket('F600BC2D8F')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 0

    packet = readPacket('9C005AC2F8F0')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 0

    packet = readPacket('9C0141080250320F1802104A08')
    result = parsePacket(packet)[0]
    result = applyRule(result)
    assert result == 1


def test_partTwo():
    result = partTwo('9C005AC2F8F0')

