import aoc

input_data = aoc.get_input()


def _max_y_pos(lower_bound, upper_bound):
    max_pos = 0
    for starting_vel in range(200):
        y_pos = 0
        local_max_pos = 0
        vel = starting_vel
        while y_pos > lower_bound:
            y_pos += vel
            if vel == 0:  # highest point
                if y_pos > local_max_pos:
                    local_max_pos = y_pos
            vel -= 1
            if upper_bound >= y_pos >= lower_bound:
                if local_max_pos > max_pos:
                    max_pos = local_max_pos
                break

    return max_pos


def _simulate(x_vel, y_vel, x_range, y_range):
    pos = [0, 0]
    # x_range[0] < pos[0] < x_range[1] and y_range[0] < pos[1] < y_range[1]
    while pos[0] <= x_range[1] and pos[1] >= y_range[0]:
        if pos[0] >= x_range[0] and pos[1] <= y_range[1]:
            return True
        pos[0] += max(x_vel, 0)
        pos[1] += y_vel

        x_vel -= 1
        y_vel -= 1

    return False


def challenge1():
    for line in input_data:
        y_range = tuple(int(a) for a in line[13:].split(', ')[1].strip('y=').split('..'))
        _max_y_pos(*y_range)


def challenge2():
    x_range = tuple(int(a) for a in input_data[0][13:].split(', ')[0].strip('x=').split('..'))
    y_range = tuple(int(a) for a in input_data[0][13:].split(', ')[1].strip('y=').split('..'))

    count = 0
    for x in range(-350, 350):
        for y in range(-350, 350):
            if _simulate(x, y, x_range, y_range):
                count += 1

    return count


aoc.run(challenge1)
aoc.run(challenge2)
