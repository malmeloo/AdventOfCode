import aoc


input_data = aoc.get_input()


def challenge1():
    fwd = 0
    depth = 0
    for line in input_data:
        cmd, factor = line.split(' ')
        if cmd == 'forward':
            fwd += int(factor)
        elif cmd == 'down':
            depth += int(factor)
        elif cmd == 'up':
            depth -= int(factor)

    return fwd * depth


def challenge2():
    fwd = 0
    depth = 0
    aim = 0
    for line in input_data:
        cmd, factor = line.split(' ')
        if cmd == 'forward':
            fwd += int(factor)
            depth += int(factor) * aim
        elif cmd == 'down':
            aim += int(factor)
        elif cmd == 'up':
            aim -= int(factor)

        # print(f'{line}: {fwd},{depth},{aim}')

    return fwd * depth


aoc.run(challenge1)
aoc.run(challenge2)
