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


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}
        self.allPaths = []

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def __findPaths(self, u, d, visited, path):
        path.append(u)
        visited[u] = True

        if u == d:
            self.allPaths.append([x for x in path])
            if debug:
                ic(path)

        else:
            for i in self.graph[u]:
                condition = (
                    visited[i] and i.islower()
                )
                if not condition:
                    self.__findPaths(i, d, visited, path)

        path.pop()
        visited[u] = False

    def findAllPaths(self, s, d):
        visited = {x: False for x in self.graph.keys()}
        path = []
        self.__findPaths(s, d, visited, path)

        return self.allPaths


def findPaths(caveConnections):

    uniqueNodes = set([x[0] for x in caveConnections]).union(
        set(x[1] for x in caveConnections)
        )

    g = Graph(len(uniqueNodes))
    for connection in caveConnections:
        g.addEdge(connection[0], connection[1])
        g.addEdge(connection[1], connection[0])

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
