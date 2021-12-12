from icecream import ic 
from typing import Dict

debug = False
def readCaveConnections(file):
    caveConnections = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            line = tuple(cave for cave in line.split('-'))
            caveConnections.append(line)
    return caveConnections


class CaveGraph:
    def __init__(self, vertices):
        uniqueNodes = set([x[0] for x in vertices]).union(
            set(x[1] for x in vertices)
            )
        self.edgeDict = {x: [] for x in uniqueNodes}

        for connection in vertices:
            self.edgeDict[connection[0]].append(connection[1])
            self.edgeDict[connection[1]].append(connection[0])

        self.allPaths = []

    def __transverseGraph(self, nextNode, endNode, visited, path):
        path.append(nextNode)
        visited[nextNode] = True

        if nextNode == endNode:
            self.allPaths.append([x for x in path])
            if debug:
                ic(path)

        else:
            for node in self.edgeDict[nextNode]:
                condition = (
                    visited[node] and node.islower()
                )
                if not condition:
                    self.__transverseGraph(node, endNode, visited, path)

        path.pop()
        visited[nextNode] = False

    def findAllPaths(self, start, end):
        visited = {x: False for x in self.edgeDict.keys()}
        path = []
        self.__transverseGraph(start, end, visited, path)

        return self.allPaths


def findPaths(caveConnections):
    g = CaveGraph(caveConnections)
    allPaths = g.findAllPaths('start', 'end')
    return allPaths


def partOne():
    caveConnections = readCaveConnections('data/data_q12.txt')
    allPaths = findPaths(caveConnections)
    statement = (
        f'There are {len(allPaths)} paths'
        )
    print(statement)
    return allPaths


def partTwo(inputData):

    '''
    visiting a single small cavern twice is
    equivalent to copying its edges, and making a new node
    '''
    allPaths = set()
    caveConnections = readCaveConnections(inputData)
    uniqueNodes = set([x[0] for x in caveConnections]).union(
        set(x[1] for x in caveConnections)
        )
    smallCaves = [x for x in uniqueNodes if x.islower()]
    smallCaves.remove('start')
    smallCaves.remove('end')

    for cave in smallCaves:
        newName = f'{cave}_repeatvisit'
        caveConnTmp = [x for x in caveConnections]
        for connection in caveConnections:
            if cave == connection[0]:
                caveConnTmp.append((newName, connection[1]))
            if cave == connection[1]:
                caveConnTmp.append((connection[0], newName))
        ic(caveConnTmp) if debug else ""
        allPathsLocal = findPaths(caveConnTmp)

        for position, path in enumerate(allPathsLocal):
            if newName in path:
                allPathsLocal[position] = [x.split('_')[0] for x in path]

            allPaths.add(tuple(allPathsLocal[position]))

        ic(allPathsLocal) if debug else ""

    ic(allPaths) if debug else ""
    statement = (
        f'There are {len(allPaths)} paths'
        )
    print(statement)
    return allPaths


partOne()
partTwo('data/data_q12.txt')
