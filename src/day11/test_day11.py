from day11q2 import timeStep


def test_timeStep():

    octopusMap = []
    octopusMapSteps = []

    with open('data/data_q11_dummy.txt', 'r') as f:
        for line in f:
            line = [int(x) for x in line.strip()]
            octopusMap.append(line)

    with open('data/data_q11_dummy_steps.txt', 'r') as f:
        octopusMapTmp = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                octopusMapSteps.append(octopusMapTmp)
                octopusMapTmp = []
            else:
                line = [int(x) for x in line.strip()]
                octopusMapTmp.append(line)
        octopusMapSteps.append(octopusMapTmp)

    fired, allfired = timeStep(octopusMap)

    assert octopusMap == octopusMapSteps[0]
    assert allfired is False
    assert fired == 0

    for count in range(0, 99):
        local_fired, _ = timeStep(octopusMap)
        fired += local_fired
    assert fired == 1656

    octopusMap = []
    with open('data/data_q11_dummy.txt', 'r') as f:
        for line in f:
            line = [int(x) for x in line.strip()]
            octopusMap.append(line)

    count = 0
    while True:
        count += 1
        if timeStep(octopusMap)[1]:
            break
        if count > 5000:
            raise Exception('More than 5000 steps')
    assert count == 195
