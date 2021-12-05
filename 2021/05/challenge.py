import aoc
import copy

input_data = aoc.get_input()
line_coords = []
for line in input_data:
    begin, end = line.split(' -> ')

    b_x = int(begin.split(',')[0])
    b_y = int(begin.split(',')[1])
    e_x = int(end.split(',')[0])
    e_y = int(end.split(',')[1])
    line_coords.append(((b_x, b_y), (e_x, e_y)))


def _interpolate_straight(coord1, coord2):
    if coord1[0] == coord2[0]:  # vertical line
        x = coord1[0]
        return [(x, y) for y in range(coord1[1], coord2[1])] + [coord2]
    if coord1[1] == coord2[1]:  # horizontal line
        y = coord1[1]
        return [(x, y) for x in range(coord1[0], coord2[0])] + [coord2]


def _interpolate_slope(coord1, coord2):
    slope = 1 if coord2[1] > coord1[1] else -1

    res = []
    cur_coord = copy.copy(coord1)
    while cur_coord != coord2:
        res.append(cur_coord)
        cur_coord = (cur_coord[0] + 1, cur_coord[1] + slope)
    res.append(coord2)

    return res


def _interpolate(coord1, coord2):
    if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
        return _interpolate_straight(coord1, coord2)
    else:
        return _interpolate_slope(coord1, coord2)


def challenge1():
    coord_count = {}

    for coord in line_coords:
        interp = _interpolate_straight(min(coord), max(coord))
        if not interp:
            continue

        for point in interp:
            coord_count[point] = coord_count.get(point, 0) + 1

    return len([p for p in coord_count.values() if p > 1])


def challenge2():
    coord_count = {}

    for coord in line_coords:
        interp = _interpolate(min(coord), max(coord))

        for point in interp:
            coord_count[point] = coord_count.get(point, 0) + 1

    return len([p for p in coord_count.values() if p > 1])


aoc.run(challenge1)
aoc.run(challenge2)
