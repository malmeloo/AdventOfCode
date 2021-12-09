import aoc

height_map = aoc.get_input('\n', data_type=lambda line: [int(c) for c in line])
to_check = [(x, y) for x in range(len(height_map[0])) for y in range(len(height_map))]


def _adjacent(x: int, y: int):
    adjacent = {}
    if x > 0:
        adjacent[(x - 1, y)] = height_map[y][x - 1]
    if x < len(height_map[0]) - 1:
        adjacent[(x + 1, y)] = height_map[y][x + 1]
    if y > 0:
        adjacent[(x, y - 1)] = height_map[y - 1][x]
    if y < len(height_map) - 1:
        adjacent[(x, y + 1)] = height_map[y + 1][x]

    return adjacent


def _is_low_point(x: int, y: int):
    point = height_map[y][x]
    adjacent = _adjacent(x, y).values()

    return all(point < p for p in adjacent)


def challenge1():
    risk_level = 0

    for y, row in enumerate(height_map):
        for x, point in enumerate(row):
            if _is_low_point(x, y):
                risk_level += point + 1

    return risk_level


def _flood_fill(x: int, y: int):
    global to_check
    if height_map[y][x] == 9 or (x, y) not in to_check:
        return
    to_check.remove((x, y))

    adj = _adjacent(x, y).keys()
    for point_x, point_y in adj:
        _flood_fill(point_x, point_y)


def challenge2():
    basins = []

    for x, y in to_check:
        old_size = len(to_check)
        _flood_fill(x, y)
        basin_size = old_size - len(to_check)

        if basin_size != 0:
            basins.append(basin_size)

    largest_basins = sorted(basins, reverse=True)[:3]

    return largest_basins[0] * largest_basins[1] * largest_basins[2]


aoc.run(challenge1)
aoc.run(challenge2)
