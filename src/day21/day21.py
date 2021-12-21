from typing import Dict, Tuple
from icecream import ic
import copy as cp
debug = False

def readData(file):
    startingPositions = []
    with open(file, 'r') as f:
        for line in f:
            line = line.split(':')[1]
            line = line.strip()
            startingPositions.append(int(line))
    return startingPositions


class DeterministicDie:
    def __init__(self) -> None:
        self.rolls = 0
        self.side = self.__sides()
        self.previousResult = 0

    def __sides(self):
        for side in range(1, 101):
            yield side

    def getSide(self):
        try:
            side = next(self.side)
        except StopIteration:
            self.side = self.__sides()
            side = next(self.side)
        # ic(f'rolled {side}')
        return side

    def roll3Times(self):
        self.rolls += 3
        result = self.getSide()
        result += self.getSide()
        result += self.getSide()
        return result


def playDeterministicGame(player1: int, player2: int):
    player1Score = 0
    player2Score = 0
    die = DeterministicDie()
    while player1Score < 1000 and player2Score < 1000:
        player1 += die.roll3Times()
        # ic(f'player1 {player1}')
        if player1 > 10:
            player1 = player1 % 10
            if player1 == 0:
                player1 = 10
        player1Score += player1
        # ic(f'player1 Score {player1Score}')
        if player1Score >= 1000:
            break
        player2 += die.roll3Times()
        # ic(f'player2 {player2}')
        if player2 > 10:
            player2 = player2 % 10
            if player2 == 0:
                player2 = 10
        player2Score += player2
        # ic(f'player2 Score {player2Score}')

    return player1Score, player2Score, die.rolls


def calcPos(position: int, move: int) -> int:
    nPosition = position + move
    if nPosition > 10:
        nPosition = nPosition % 10
        if nPosition == 0:
            nPosition = 1
    return nPosition


def playQuantumGame(player1Start: int, player2Start: int):
    maxScore = 21
    # we can go up to 20 + a move of 10 so 30
    # dictionary keys is (player1Pos, player1Score, player2Pos, Player2Score)
    # value is number of games with that configuration
    emptyDict = {}
    for player1pos in range(1, 11):
        for player2pos in range(1, 11):
            for s1 in range(0, maxScore + 11):
                for s2 in range(0, maxScore + 11):
                    index = (player1pos, s1, player2pos, s2)
                    emptyDict[index] = 0

    prv = cp.deepcopy(emptyDict)
    prv[(player1Start, 0, player2Start, 0)] = 1

    # when we make a move, we move each player to + 1, 2, and 3
    # of their current position, and scores depending on the position
    # they land on
    i = 0
    hasValue = True
    pList = []
    pList1 = [3, 4, 5, 4, 5, 6, 5, 6, 7]
    pList2 = [4, 5, 6, 5, 6, 7, 6, 7, 8]
    pList3 = [5, 6, 7, 6, 7, 8, 7, 8, 9]
    pList.extend(pList1)
    pList.extend(pList2)
    pList.extend(pList3)
    pDict = {}
    for value in pList:
        if value not in pDict.keys():
            pDict[value] = 1
        else:
            pDict[value] += 1

    assert len(pList) == 27
    while hasValue:
        # start with an empty dict for the next move
        nMove = cp.deepcopy(emptyDict)
        i += 1
        # print(i)
        # loop through previous dict
        hasValue = False
        for key, value in prv.items():
            p1 = key[0]
            s1 = key[1]
            p2 = key[2]
            s2 = key[3]
            if s2 >= 21 and s1 >= 21:
                if value != 0:
                    raise Exception('There should be nothing here')
                else:
                    continue
            if s2 >= 21 or s1 >= 21:
                nMove[(p1, s1, p2, s2)] += value
                continue
            # if we have a gamestate that looks like this:
            if value > 0 and s1 < 21 and s2 < 21:
                hasValue = True
                for o1, rept in pDict.items():
                    np1 = calcPos(p1, o1)
                    ns1 = s1 + np1
                    if ns1 >= 21:
                        nMove[(np1, ns1, p2, s2)] += rept * value
                    else:
                        for o2, rept2 in pDict.items():
                            np2 = calcPos(p2, o2)
                            ns2 = s2 + np2
                            nMove[(np1, ns1, np2, ns2)] += rept * rept2 * value
        if debug:
            nonzero = 0
            for key, value in nMove.items():
                if value != 0:
                    nonzero += value
            statement = (
                f'There are {nonzero} universe after {i} rounds. '
                f'All games complete: {not hasValue}')
            print(statement)
        prv = cp.deepcopy(nMove)
        if i > 500:
            raise Exception('too many iteration')
    return nMove


def countQuantumGame(gameDict: Dict) -> Tuple:
    maxScore = 21
    numWonBy2 = 0
    numWonBy1 = 0
    for key, value in gameDict.items():
        p1 = key[0]
        s1 = key[1]
        p2 = key[2]
        s2 = key[3]
        if s2 >= 21:
            numWonBy2 += value
        if s1 >= 21:
            numWonBy1 += value
        if s2 >= 21 and s1 >= 21 and value != 0:
            print(f'Dict[({p1},{s1},{p2},{s2})] = {value}')
            raise Exception('This can not happen, tie?')
        if s2 < 21 and s1 < 21 and value != 0:
            print(f'Dict[({p1},{s1},{p2},{s2})] = {value}')
            raise Exception('This should not happen, no one won')

    return numWonBy1, numWonBy2


def partOne(data):
    player1, player2 = readData(data)
    player1S, player2S, nRolls = playDeterministicGame(
        player1, player2)
    if player2S > player1S:
        winning = player2S
        lossing = player1S
    else:
        winning = player1S
        lossing = player2S

    statement = (
        f'The lossing player scored {lossing} in {nRolls} rolls.\n'
        f'The product is {lossing * nRolls}'
    )
    print(statement)
    return lossing * nRolls


def partTwo(data):
    player1, player2 = readData(data)
    gameResults = playQuantumGame(player1, player2)
    nWon1, nWon2 = countQuantumGame(gameResults)
    statement = (
        f'player 1 won {nWon1} out of {nWon1 + nWon2}\n'
        f'player 2 won {nWon2} out of {nWon1 + nWon2}'
    )
    print(statement)
    return max([nWon1, nWon2])


if __name__ == '__main__':
    partOne('data/data_q21.txt')
    partTwo('data/data_q21.txt')
