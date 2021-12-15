def readCaveMap(file):
    caveMap = []
    with open(f'{file}', 'r') as f:
        for line in f:
            line = [int(x) for x in line.strip()]
            caveMap.append(line)

    return caveMap


class CaveNode:
    def __init__(self, parent=None, position=None, cost=1):
        self.parent = parent
        self.position = position

        self.value = cost
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, __o: object) -> bool:
        return self.position == __o.position

    def __repr__(self) -> str:
        return f'({self.position[0]}, {self.position[1]})'

    def __lt__(self, __o: object):
        return self.f < __o.f

    def get_cost(self):
        return self.value

    def __hash__(self) -> int:
        return hash(repr(self))


def neighbors(caveMap, node) -> CaveNode:

    np = getattr(node, 'position')
    ml = len(caveMap) - 1

    if np[0] > 0:
        yield CaveNode(
                node,
                (np[0] - 1, np[1]),
                caveMap[np[0] - 1][np[1]]
                )
    if np[0] < ml:
        yield CaveNode(
                node,
                (np[0] + 1, np[1]),
                caveMap[np[0] + 1][np[1]]
                )

    if np[1] > 0:
        yield CaveNode(
                node,
                (np[0], np[1] - 1),
                caveMap[np[0]][np[1] - 1]
                )
    if np[1] < ml:
        yield CaveNode(
                node,
                (np[0], np[1] + 1),
                caveMap[np[0]][np[1] + 1]
                )


def findCavePath(caveMap, start, end):

    startNode = CaveNode(None, start, caveMap[start[0]][start[1]])
    setattr(startNode, 'g', 0)
    setattr(startNode, 'h', 0)
    setattr(startNode, 'f', 0)

    endNode = CaveNode(None, end, caveMap[end[0]][end[1]])
    setattr(endNode, 'g', 0)
    setattr(endNode, 'h', 0)
    setattr(endNode, 'f', 0)

    openList = []
    closedList = set()

    openList.append(startNode)

    while len(openList) > 0:
        openList.sort(reverse=False)
        currentNode = openList[0]
        openList.pop(0)
        closedList.add(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(getattr(current, 'position'))
                current = getattr(current, 'parent')
            return path[::-1]

        # Loop through children
        for child in neighbors(caveMap, currentNode):
            # Child is on the closed list
            if child in closedList:
                continue

            # Create the f, g, and h values
            setattr(child, 'g', getattr(currentNode, 'g') + child.get_cost())
            setattr(child, 'h', 0)
            setattr(child, 'f', getattr(child, 'g') + getattr(child, 'h'))
            # Child is already in the open list
            if child in openList:
                position = openList.index(child)
                if openList[position].g > child.g:
                    openList.pop(position)
                    openList.append(child)
                continue
            # Add the child to the open list
            openList.append(child)


def calculateCost(caveMap, start, end):
    path = findCavePath(caveMap, start, end)
    cost = 0
    for node in path[1:]:
        cost += caveMap[node[0]][node[1]]
    return path, cost


def increaseMapSize(caveMap, multi):
    newCaveMap = []
    for yOffset in range(multi):
        for y in range(len(caveMap)):
            row = []
            for offset in range(multi):
                values = [x + offset + yOffset for x in caveMap[y]]
                for value in values:
                    if value > 9:
                        value = value % 10 + 1
                    row.append(value)
            newCaveMap.append(row)
    return newCaveMap


def partOne(data):
    caveMap = readCaveMap(data)
    lowerCorner = (len(caveMap) - 1, len(caveMap[-1]) - 1)
    cheapest = calculateCost(caveMap, (0, 0), lowerCorner)
    statement = (
        f'the cheapest path has a cost of {cheapest[1]}'
    )
    print(statement)
    return cheapest


def partTwo(data):
    caveMap = readCaveMap(data)
    caveMap = increaseMapSize(caveMap, 5)
    lowerCorner = (len(caveMap) - 1, len(caveMap[-1]) - 1)
    cheapest = calculateCost(caveMap, (0, 0), lowerCorner)
    statement = (
        f'the cheapest path has a cost of {cheapest[1]}'
    )
    print(statement)
    return cheapest


if __name__ == '__main__':
    partOne('data/data_q15.txt')
    partTwo('data/data_q15.txt')
