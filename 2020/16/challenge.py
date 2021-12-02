import aoc

# get cube using init_state[z][y][x]
init_state = [aoc.get_example(data_type=list)]


def cubes():
    for z, z_row in enumerate(init_state):
        for y, y_row in enumerate(z_row):
            for x, cube in enumerate(y_row):
                yield cube, (x, y, z)


def get_cube(coords):
    try:
        return init_state[coords[2]][coords[1]][coords[0]]
    except IndexError:  # cube out of bounds, so it is inactive
        return '.'


def set_cube(coords, value):
    cur_x_size = len(init_state[0][0])
    cur_y_size = len(init_state[0])
    cur_z_size = len(init_state)

    # expand z down
    if coords[2] < 0:
        new_layer = [['.'] * cur_x_size] * cur_y_size
        for _ in range(-coords[2]):
            init_state.insert(0, new_layer)
    # expand z up
    elif coords[2] >= cur_z_size:
        new_layer = [['.'] * cur_x_size] * cur_y_size
        for _ in range(coords[2] - cur_z_size + 1):
            init_state.append(new_layer)
    cur_z_size = len(init_state)

    # expand y up
    if coords[1] < 0:
        new_layer = ['.'] * cur_x_size
        for z in range(cur_z_size):
            for _ in range(-coords[1]):
                init_state[z].insert(0, new_layer)
    # expand y down
    elif coords[1] >= cur_y_size:
        new_layer = ['.'] * cur_x_size
        for z in range(cur_z_size):
            for _ in range(coords[1] - cur_y_size + 1):
                init_state[z].append(new_layer)
    cur_y_size = len(init_state[0])

    # expand x up
    if coords[0] < 0:
        for z in range(cur_z_size):
            for y in range(cur_y_size):
                for _ in range(-coords[0]):
                    init_state[z][y].insert(0, '.')
    # expand x down
    elif coords[0] >= cur_y_size:
        for z in range(cur_z_size):
            for y in range(cur_y_size):
                for _ in range(coords[0] - cur_x_size + 1):
                    init_state[z][y].append('.')

    init_state[coords[2]][coords[1]][coords[0]] = value


def neighbors(coords):
    res = []

    for x in range(coords[0]-1, coords[0]+2):
        for y in range(coords[1] - 1, coords[1] + 2):
            for z in range(coords[2] - 1, coords[2] + 2):
                cube_coords = (x, y, z)
                res.append((get_cube(cube_coords), cube_coords))

    return res


def cycle():
    to_check = set()
    for cube in cubes():
        for neighbor in neighbors(cube[1]):
            to_check.add(neighbor[1])

    for cube in to_check:
        set_cube(cube, '#')

    print_state()


def print_state():
    print(len(init_state))

    for z_layer in init_state:
        for y_layer in z_layer:
            print(''.join(y_layer))
    print()


def challenge1():
    for _ in range(1):
        cycle()


aoc.run(challenge1)
