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

class Image:
    def __init__(self, image: List[str], algo: str):
        self.image = image
        self.orginalImage = copy.deepcopy(image)
        self.algo = algo
        self.nEnh = 0
        

    def convertToDecimal(self, pixels: str):
        pixels = pixels.replace('.', '0')
        pixels = pixels.replace('#', '1')
        result = int(pixels, 2)
        return result

    def enhanceImage(self):
        outputImage = []
        inputImage = copy.deepcopy(self.image)
        if self.nEnh % 2 == 1 and self.algo[0] == '#':
            padWith = '#'
        else:
            padWith = '.'
        self.nEnh += 1
        toPad = padWith * len(inputImage)
        inputImage.append(toPad)
        inputImage.append(toPad)
        inputImage.insert(0, toPad)
        inputImage.insert(0, toPad)
        farthestLeft = 99999
        farthestRight = 0
        for y, row in enumerate(inputImage):
            row = padWith + padWith + row + padWith + padWith
            inputImage[y] = row
        for y in range(1, len(inputImage) - 1):
            outputrow = ''
            row = inputImage[y]
            for x in range(1, len(row) - 1):
                pixel = inputImage[y][x]
                left = inputImage[y][x - 1]
                upper = inputImage[y - 1][x]
                upperLeft = inputImage[y - 1][x - 1]
                upperRight = inputImage[y - 1][x + 1]
                right = inputImage[y][x + 1]
                lowerRight = inputImage[y + 1][x + 1]
                lower = inputImage[y + 1][x]
                lowerLeft = inputImage[y + 1][x - 1]

                ninePixels = (
                    upperLeft + upper + upperRight +
                    left + pixel + right +
                    lowerLeft + lower + lowerRight)

                algoLoc = self.convertToDecimal(ninePixels)
                outputrow = outputrow + self.algo[algoLoc]
            '''
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
            '''
            outputImage.append(outputrow)

        self.image = outputImage

    def countLitPixels(self):
        lit = 0
        for row in self.image:
            lit += row.count('#')

        return lit


def partOne(data):
    algo, image = readInput(data)
    myImage = Image(image, algo)
    myImage.enhanceImage()
    myImage.enhanceImage()
    lit = myImage.countLitPixels()
    statement = (
        f'{lit} pixels are lit'
    )
    print(statement)
    return lit


def partTwo(data):
    algo, image = readInput(data)
    myImage = Image(image, algo)
    for _ in range(50):
        myImage.enhanceImage()
    lit = myImage.countLitPixels()
    statement = (
        f'{lit} pixels are lit after 50 enhancements'
    )
    print(statement)
    return lit

if __name__ == '__main__':
    partOne('data/data_q20.txt')
    partTwo('data/data_q20.txt')
