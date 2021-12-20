from typing import List
import copy
from icecream import ic

def readInput(file: str):
    image = []
    with open(f'{file}', 'r') as f:
        algorithm = f.readline().strip()
        for line in f:
            line = line.strip()
            if len(line) > 0:
                image.append(line)

    return algorithm, image


def convertToDecimal(pixels: str):
    pixels = pixels.replace('.', '0')
    pixels = pixels.replace('#', '1')
    result = int(pixels, 2)
    return result


def enhanceImage(inputImage_: List[List[str]], algo: str):
    outputImage = []
    inputImage = copy.deepcopy(inputImage_)
    toPady = '.' * len(inputImage)
    inputImage.append(toPady)
    inputImage.insert(0, toPady)
    yMax = len(inputImage) - 1
    farthestLeft = 99999
    farthestRight = 0
    for y, in range(1, len(inputImage)):
        row = inputImage[y] 
        row = '.' + row + '.'
        for x, in range(1, len(row))
            # left
            if x != 0:
                left = inputImage[y][x - 1]
            else:
                left = '.'
            # above
            if y != 0:
                upper = inputImage[y - 1][x]
            else:
                upper = '.'
            # upper left
            if x != 0 and y != 0:
                upperLeft = inputImage[y - 1][x - 1]
            else:
                upperLeft = '.'
            # upper right
            if x != xMax and y != 0:
                upperRight = inputImage[y - 1][x + 1]
            else:
                upperRight = '.'
            # right
            if x != xMax:
                right = inputImage[y][x + 1]
            else:
                right = '.'
            # lower right
            if x != xMax and y != yMax:
                lowerRight = inputImage[y + 1][x + 1]
            else:
                lowerRight = '.'
            # lower
            if y != yMax:
                lower = inputImage[y + 1][x]
            else:
                lower = '.'
            # lower left
            if y != yMax and x != 0:
                lowerLeft = inputImage[y + 1][x - 1]
            else:
                lowerLeft = '.'

            ninePixels = (
                upperLeft + upper + upperRight +
                left + pixel + right +
                lowerLeft + lower + lowerRight)

            algoLoc = convertToDecimal(ninePixels)
            outputrow = outputrow + algo[algoLoc]
        localLeft = outputrow.find('#')
        localRight = outputrow[::-1].find('#')
        if localRight != -1:
            localRight = len(row) - localRight
            if localRight > farthestRight:
                farthestRight = localRight
        if localLeft != -1:
            if localLeft < farthestLeft:
                farthestLeft = localLeft
        outputImage.append(outputrow)

    anyontop = outputImage[0].find('#')
    if anyontop == -1:
        outputImage.pop(0)
    anyonbottom = outputImage[-1].find('#')
    if anyonbottom == -1:
        outputImage.pop(-1)
    for n, row in enumerate(outputImage):
        outputImage[n] = row[farthestLeft:farthestRight]
    # print(outputImage)
    return outputImage


def countLitPixels(image: List[str]):
    lit = 0
    for row in image:
        lit += row.count('#')

    return lit


def partOne(data):
    algo, image = readInput(data)
    outputImage = enhanceImage(image, algo)
    outputImage = enhanceImage(outputImage, algo)
    lit = countLitPixels(outputImage)
    statement = (
        f'{lit} pixels are lit'
    )
    print(statement)
    for row in outputImage:
        print(row)
    return lit


if __name__ == '__main__':
    partOne('data/data_q20.txt')
