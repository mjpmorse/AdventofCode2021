aim = 0
depth = 0
position = 0

with open('data/data_q2.txt', 'r') as f:
    for line in f:
        command = line.split(' ')
        if command[0] == 'down':
            aim += int(command[1])

        elif command[0] == 'up':
            aim -= int(command[1])

        elif command[0] == 'forward':
            position += int(command[1])
            depth += aim * int(command[1])

print(f"move down {depth} units and forward {position} units")
print(f"The product is {depth * position}")
