from day18 import readHomeWork, explodeNumber, splitNumber, addNumbers
from day18 import SnailFishNumber, magnitude, partOne


def test_readHomework():
    homeWork = readHomeWork('data/data_q18_dummy.txt')
    assert len(homeWork) == 10
    assert homeWork[7] == '[[9,3],[[9,9],[6,[4,9]]]]'


def test_explodeNumber():
    assert explodeNumber('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
    assert explodeNumber('[[1,2],[3,4]]') == '[[1,2],[3,4]]'
    assert explodeNumber('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
    assert explodeNumber('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
    assert explodeNumber('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') ==\
        '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    assert explodeNumber('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') ==\
        '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'


def test_splitNumber():
    assert splitNumber([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]) == \
        [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    assert splitNumber([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]) == \
        [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]


def test_addNumbers():
    a = SnailFishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = SnailFishNumber('[1,1]')
    c = SnailFishNumber('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert addNumbers(a, b) == c

    a = SnailFishNumber('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
    b = SnailFishNumber('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
    c = SnailFishNumber('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
    assert addNumbers(a, b) == c

    a = SnailFishNumber('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
    b = SnailFishNumber('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]')
    c = SnailFishNumber('[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]')
    assert addNumbers(a, b) == c

    a = SnailFishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = SnailFishNumber('[1,1]')
    c = SnailFishNumber('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert addNumbers(a, b) == c

    a = SnailFishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = SnailFishNumber('[1,1]')
    c = SnailFishNumber('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert addNumbers(a, b) == c

    a = SnailFishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = SnailFishNumber('[1,1]')
    c = SnailFishNumber('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert addNumbers(a, b) == c

    a = SnailFishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = SnailFishNumber('[1,1]')
    c = SnailFishNumber('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert addNumbers(a, b) == c

def test_magnitude():
    assert magnitude([[1,2],[[3,4],5]]) == 143
    assert magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
    assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

# def test_partOne():
#     assert partOne('data/data_q18_dummy.txt') == 4140
