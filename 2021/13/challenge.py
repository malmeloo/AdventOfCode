import copy

import aoc

_coords, _folds = aoc.get_input('\n\n')
dot_coords = set(tuple(int(a) for a in line.split(',')) for line in _coords.splitlines())
folds = [tuple(line.split(' ')[-1].split('=')) for line in _folds.splitlines()]


def _fold_x(coords: set, x: int):
    coords_copy = set()
    for coord in coords:
        if coord[0] > x:
            new_coord = (x - (coord[0] - x), coord[1])
        else:
            new_coord = coord
        coords_copy.add(new_coord)

    return coords_copy


def _fold_y(coords: set, y: int):
    coords_copy = set()
    for coord in coords:
        if coord[1] > y:
            new_coord = (coord[0], y - (coord[1] - y))
        else:
            new_coord = coord
        coords_copy.add(new_coord)

    return coords_copy


def _bbox(coords: set):
    max_x = 0
    max_y = 0
    for x, y in coords:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return max_x, max_y


def challenge1():
    fold = folds[0]
    res = 0
    if fold[0] == 'x':
        res = len(_fold_x(dot_coords, int(fold[1])))
    elif fold[0] == 'y':
        res = len(_fold_y(dot_coords, int(fold[1])))

    return res


def challenge2():
    res = copy.copy(dot_coords)
    for fold in folds:
        if fold[0] == 'x':
            res = _fold_x(res, int(fold[1]))
        elif fold[0] == 'y':
            res = _fold_y(res, int(fold[1]))

    bbox = _bbox(res)
    for y in range(bbox[1] + 1):
        for x in range(bbox[0] + 1):
            if (x, y) in res:
                print('#', end='')
            else:
                print(' ', end='')
        print()


aoc.run(challenge1)
aoc.run(challenge2)
