from icecream import ic
from typing import List, Tuple

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
    def __init__(self, edges: List[Tuple], numVisits={}):
        """ A graph representation of the cave.
        The graph is adirectional based the list of edges.
        Nodes with lowercase names can be visited one in a transversal
        Nodes with uppercase names can be visited any number of times.
        This can be overridden by passing the name and number of visits
        in numVisits dictionary.

        Args:
            edges (List[Tuple]): List of the edges in tuple form.
            numVisits (dict, optional): Override default visit behavior.
                e.g. {'A': 1} would only allow node 'A' to be visited once.
                Defaults to {}.
        """
        uniqueNodes = set([x[0] for x in edges]).union(
            set(x[1] for x in edges)
            )
        self.edgeDict = {x: [] for x in uniqueNodes}

        for connection in edges:
            self.edgeDict[connection[0]].append(connection[1])
            self.edgeDict[connection[1]].append(connection[0])

        self.allPaths = []
        self.maxVisits = {x: 1 if x.islower() else -1 for x in uniqueNodes}
        for node, visits in numVisits.items():
            self.maxVisits[node] = visits

    def __transverseGraph(self, nextNode, endNode, visited, path):
        path.append(nextNode)
        visited[nextNode] += 1

        if nextNode == endNode:
            self.allPaths.append([x for x in path])
            if debug:
                ic(path)

        else:
            for node in self.edgeDict[nextNode]:
                condition = (
                    visited[node] < self.maxVisits[node] or
                    self.maxVisits[node] == -1
                )
                if condition:
                    self.__transverseGraph(node, endNode, visited, path)

        path.pop()
        visited[nextNode] -= 1

    def findAllPaths(self, start, end):
        visited = {x: False for x in self.edgeDict.keys()}
        path = []
        self.__transverseGraph(start, end, visited, path)

        return self.allPaths


def findPaths(caveConnections, **kwargs):
    g = CaveGraph(caveConnections, **kwargs)
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
        allPathsLocal = findPaths(caveConnections, numVisits={cave: 2})
        for path in allPathsLocal:
            allPaths.add(tuple(path))

        ic(allPathsLocal) if debug else ""

    ic(allPaths) if debug else ""
    statement = (
        f'There are {len(allPaths)} paths'
        )
    print(statement)
    return allPaths


partOne()
partTwo('data/data_q12.txt')
