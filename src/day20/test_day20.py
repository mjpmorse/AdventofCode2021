from day20 import readInput, convertToDecimal, enhanceImage, partOne


def test_readInput():
    algo, image = readInput('data/data_q20_dummy.txt')

    assert len(algo) == 512
    assert len(image) == 5
    for row in image:
        assert len(row) == 5


def test_convertToDecimal():
    assert convertToDecimal('...#...#.') == 34


def test_enhanceImage():
    algo, image = readInput('data/data_q20_dummy.txt')
    outputImage = enhanceImage(image, algo)
    assert outputImage[0] == '.##.##.'
    assert outputImage[1] == '#..#.#.'
    assert outputImage[2] == '##.#..#'
    assert outputImage[-1] == '...#.#.'


def test_partOne():
    assert partOne('data/data_q20_dummy.txt') == 35
