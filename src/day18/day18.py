from ast import literal_eval 
from typing import List
import copy
from time import sleep
from icecream import ic


def readHomeWork(file):
    homeWork = []
    with open(f'{file}', 'r') as f:
        for line in f:
            line = line.strip()
            homeWork.append(line)

    return homeWork


def explodeNumber(snailNumber):
    openCount = 0
    toAddLeft = None
    insertedAt = None
    for pos, char in enumerate(snailNumber):
        if char == '[':
            openCount += 1
        if char == ']':
            openCount -= 1
        try:
            int(char)
        except ValueError:
            pass
        if openCount > 4:
            # check we have found number
            try:
                # assumed single digit !!!
                # find next comma
                if snailNumber[pos] == '[':
                    next_comma = snailNumber.find(',', pos)
                    next_close = snailNumber.find(']', pos)
                    toAddLeft = int(snailNumber[pos + 1: next_comma])
                    toAddRight = int(snailNumber[next_comma + 1:next_close])
                    snailNumber = snailNumber[:pos]\
                        + '0' + snailNumber[next_close+1:]
                    insertedAt = pos
                    break
            except IndexError:
                continue
            except ValueError:
                continue

    if insertedAt is None:
        return snailNumber

    eval_indexs = []
    for pos, number in enumerate(snailNumber):
        try:
            int(number)
            eval_indexs.append(pos)
        except ValueError:
            continue

    # find the list closest to the insert
    listIndex = eval_indexs.index(insertedAt)
    if listIndex != len(eval_indexs) - 1:
        toTheRight = eval_indexs[listIndex + 1:]
        closestOnRightF = lambda toTheRight : toTheRight - insertedAt
        closestOnRight = min(toTheRight, key=closestOnRightF)
        farthestRight = closestOnRight
        # in case we have multiple length numbers
        for i in range(1, len(toTheRight) + 1):
            if closestOnRight + i in toTheRight:
                farthestRight = closestOnRight + i
            else:
                break
        # ic(toTheRight)
        # ic(f'{closestOnRight} {farthestRight}')
        # ic(snailNumber)
        # ic(snailNumber[closestOnRight:farthestRight + 1])
        snailNumber = snailNumber[:closestOnRight] +\
            f'{int(snailNumber[closestOnRight:farthestRight + 1]) + toAddRight}'\
            + snailNumber[farthestRight + 1:]

    if listIndex != 0:
        toTheLeft = eval_indexs[: listIndex]
        closestOnLeftF = lambda toTheLeft : insertedAt - toTheLeft
        closestOnLeft = min(toTheLeft, key=closestOnLeftF)
        farthestLeft = closestOnLeft   
        # in case we have multiple length numbers
        for i in range(1, len(toTheLeft) + 1):
            if closestOnLeft - i in toTheLeft:
                farthestLeft = closestOnLeft - i
            else:
                break
        # ic(toTheLeft)
        # ic(f'{closestOnLeft} {farthestLeft}')
        # ic(snailNumber)
        # ic(snailNumber[farthestLeft:closestOnLeft + 1])
        snailNumber =\
            snailNumber[:farthestLeft] +\
            f'{int(snailNumber[farthestLeft:closestOnLeft + 1]) + toAddLeft}' +\
            snailNumber[closestOnLeft + 1:]

    return snailNumber


def magnitude_helper(number: List) -> List:

    if all([isinstance(x, int) for x in number]):
        if len(number) != 2:
            raise Exception('This should not happen')
        return (3 * number[0] + 2 * number[1])

    for pos, num in enumerate(number):
        if isinstance(num, list):
            number[pos] = magnitude_helper(num)

    return number


def magnitude(number: List) -> int:
    i = 0
    while not isinstance(number, int) and i < 5000:
        i += 1
        number = magnitude_helper(number)
    
    return number


def splitNumber(snailNumber: List, hasSplit=False) -> List:
    for pos, number in enumerate(snailNumber):
        if hasSplit:
            break
        if isinstance(number, int):
            if number >= 10:
                hasSplit = True
                if number % 2 == 0:
                    snailNumber[pos] = [number // 2, number // 2]
                else:
                    snailNumber[pos] = [number // 2, number // 2 + 1]
                break

        else:
            snailNumber[pos], hasSplit = splitNumber(snailNumber[pos], hasSplit)

    return (snailNumber, hasSplit)

class SnailFishNumber:
    def __init__(self, number: str):
        self.snail_number = number
        self.changed = False

    def __eq__(self, __o: object) -> bool:
        return self.snail_number == __o.snail_number

    def __repr__(self) -> str:
        return f'{self.snail_number}'

    def explode(self):
        tmp_snail_nbr = copy.deepcopy(self.snail_number)
        self.snail_number = explodeNumber(self.snail_number)
        if tmp_snail_nbr == self.snail_number:
            self.changed = False
        else:
            self.changed = True

    def splitNumber(self):
        number = literal_eval(self.snail_number)
        number2 = copy.deepcopy(number)
        number = splitNumber(number)[0]
        self.snail_number = str(number).replace(" ", '')
        if number2 == number:
            self.changed = False
        else:
            self.changed = True


def addNumbers(aOrg: SnailFishNumber,
               bOrg: SnailFishNumber) -> SnailFishNumber:

    newNumber = SnailFishNumber(
        f'[{aOrg.snail_number},{bOrg.snail_number}]')
    newNumberOrg = SnailFishNumber(
        f'[{aOrg.snail_number},{bOrg.snail_number}]')
    counter = 0
    # print(f'after addition: {newNumber.snail_number}')
    first = True
    while newNumber.changed or first:
        first = False
        counter += 1
        newNumber.explode()
        if newNumber.changed:
            # print(f'after explode: {(newNumber.snail_number)}')
            # sleep(1)
            continue
        newNumber.splitNumber()
        if newNumber.changed:
            # print(f'after split:   {newNumber.snail_number}')
            continue
        if counter > 10000:
            print(newNumber)
            print(newNumberOrg)
            raise Exception('Something is wrong, too many iterations')
    return newNumber


def partOne(data):
    hw = readHomeWork(data)
    a = SnailFishNumber(hw[0])
    length = len(hw)
    for pos, number in enumerate(hw[1:]):
        print(f"on line {pos} of {length}")
        print(number)
        b = SnailFishNumber(number)
        a = addNumbers(a, b)

    print(a.snail_number)
    mag = magnitude(eval(a.snail_number))
    statement = (
        f'The magnitude of the hw is {mag}'
    )
    print(statement)
    return mag

def partTwo(data):
    hw = readHomeWork(data)
    highest_sum = 0
    for num1 in range(0, len(hw)):
        for num2 in range(num1 + 1, len(hw)):
            a = SnailFishNumber(hw[num1])
            b = SnailFishNumber(hw[num2])
            c = addNumbers(a, b)
            magc = magnitude(eval(c.snail_number))
            d = addNumbers(b, a)
            magd = magnitude(eval(d.snail_number))
            if magc > highest_sum:
                highest_sum = magc
            if magd > highest_sum:
                highest_sum = magd

    statement = (
        f'The greatest magnitude of the hw is {highest_sum}'
    )
    print(statement)
    return highest_sum


if __name__ == '__main__':
    # partOne('data/data_q18.txt')
    partTwo('data/data_q18.txt')

