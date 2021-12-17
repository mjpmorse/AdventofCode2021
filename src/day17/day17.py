from typing import List, Tuple
from icecream import ic


def readTarget(file):
    try:
        target = ''
        with open(f'{file}', 'r') as f:
            target = f.readline().strip()

    except FileNotFoundError:
        target = file.strip()

    target = target.split(':')[1]
    target = target.strip()
    target = target.split(',')
    targetX = target[0].strip()
    targetY = target[1].strip()
    targetX = targetX.split('x=')[1]
    targetY = targetY.split('y=')[1]
    targetX = targetX.split('..')
    targetY = targetY.split('..')
    rangeX = [x for x in range(int(targetX[0]), int(targetX[1]) + 1)]
    rangeY = [y for y in range(int(targetY[0]), int(targetY[1]) + 1)]

    return (rangeX, rangeY)


def bestInitialVx(rangX: List[int]) -> int:
    """ This function will calculate the
        lowest velocity such that we reach the
        left side of the allowed range.
        To do this we find the initial velocity
        such that after we have arrive at that side,
        our velocity is zero

    Args:
        rangX (List[int]): allowed x range

    Returns:
        int: optimal vx0 to achieve shortest x flight path
    """
    deltaX = rangX[0]
    vX = (2 * deltaX)**(0.5)
    # floor function
    vX = int(vX)
    return vX


def bestInitialY(rangeY: List[int]) -> int:
    """ We want to hit the lower square with
    velocity as close to the the value of that square
    as possible, this is because we want all the distance
    from start (0) to lower bound on rangeY to have
    been covered in the last time step

    Args:
        rangeY (List[int]): allowed y range

    Returns:
        int: optimal y initial velocity to achieve highest flight
    """
    target = rangeY[0]
    v_f = rangeY[0]

    v_0 = (v_f**2 + 2 * target)**(0.5)

    # we want to ceiling function of this
    if abs(v_0 % int(v_0)) > 0.00001:
        v_0 = int(v_0) + 1
    else:
        v_0 = int(v_0)
    return v_0


def maximalInitialXY(rangeX: List[int], rangeY: List[int]) -> Tuple[int]:
    """Returns the initial X, Y velocity such that the probe hits the
    lower right hand corner in one timestep
    Max vX
    Min vY (most negative)

    Args:
        rangeX (List[int]): x target range
        rangeY (List[int]): y target range

    Returns:
        Tuple[int]: (vx0, xy0) to hit lower right hand corner in one step
    """

    return (rangeX[-1], rangeY[0])


def trajectory(
        vX0: int, vY0: int,
        rangeX: List[int], rangeY: List[int]) -> List[Tuple] or None:
    """Calculate the trajectory given a initial x, y velocity.
       Ends when position is in the target area.

    Args:
        vX0 (int): initial x velocity
        vY0 (int): initial y velocity
        rangeX (List[int]): target x range
        rangeY (List[int]): target y range

    Returns:
        List[Tuple] or None: list of positions, or None if
        the initial conditions result in never landing in range.
    """

    x = 0
    y = 0
    t = 0
    vX = vX0
    vY = vY0
    path = [(0, 0)]
    # if we go past left x we have gone to far
    # if we go below bottom y we have gone to far
    while x <= rangeX[-1] and (y >= rangeY[0]):
        t = t + 1
        x = x + vX
        y = y + vY
        path.append((x, y))
        # ic(f'TimeStep {t}, (x, y): ({x},{y})')
        if x in rangeX and y in rangeY:
            return path

        if vX > 0:
            vX = vX - 1
        elif vX < 0:
            vX = vX + 1

        vY = vY - 1

    return None


def findAllIV(rangeX: List[int], rangeY: List[int]) -> List[Tuple[int]]:

    allIV = []
    maxVx, minVy = maximalInitialXY(rangeX, rangeY)
    maxVy = bestInitialY(rangeY)
    minVx = bestInitialVx(rangeX)
    for vx in range(minVx, maxVx + 1):
        for vy in range(minVy, maxVy + 1):
            if trajectory(vx, vy, rangeX, rangeY) is not None:
                allIV.append((vx, vy))
                # print(f'{vx},{vy}')
    return allIV


def partOne(data: str) -> int:
    """ Calculates the trajectory with maximal height,
    based off the input data.

    Args:
        data (str): input data

    Returns:
        int: maximal height
    """
    rangeX, rangeY = readTarget(data)
    vx0 = bestInitialVx(rangeX)
    vy0 = bestInitialY(rangeY)
    path = trajectory(vx0, vy0, rangeX, rangeY)
    yValues = [x[1] for x in path]
    maxY = max(yValues)
    statement = (
        f'The maximal height is {maxY}'
    )
    print(statement)
    return maxY


def partTwo(data):
    rangeX, rangeY = readTarget(data)
    allIV = findAllIV(rangeX, rangeY)
    statement = (
        f'There are {len(allIV)} possible initial conditions'
    )
    print(statement)
    return len(allIV)


if __name__ == '__main__':
    partOne('data/data_q17.txt')
    partTwo('data/data_q17.txt')
