import aoc
import copy

input_data = aoc.get_input()

black_tiles = set()
coord_commands = {
    'e':  (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),

    'w':  (-1, 1, 0),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1)
}


def add_coords(coord1, coord2):
    return (
        coord1[0] + coord2[0],
        coord1[1] + coord2[1],
        coord1[2] + coord2[2]
    )


def parse_line(line: str):
    final_coord = (0, 0, 0)

    while line:
        for cmd in coord_commands.keys():
            if line.startswith(cmd):
                final_coord = add_coords(final_coord, coord_commands[cmd])
                line = line[len(cmd):]

                break

    return final_coord


def flip_tile(coord):
    if coord not in black_tiles:
        black_tiles.add(coord)
    else:
        black_tiles.remove(coord)


def are_adjacent(coord1, coord2):
    diff = (
        coord1[0] - coord2[0],
        coord1[1] - coord2[1],
        coord1[2] - coord2[2]
    )

    return diff in coord_commands.values()


def adjacent_tiles(coord):
    return [add_coords(coord, diff) for diff in coord_commands.values()]


def tiles_to_search():
    res = copy.copy(black_tiles)
    for coord in black_tiles:
        res = res | set(adjacent_tiles(coord))

    return res


def should_flip(coord):
    adjacent = set(adjacent_tiles(coord))

    if coord in black_tiles:  # tile is black
        adj_count = len(adjacent & black_tiles)
        if adj_count == 0 or adj_count > 2:
            return True
    else:  # tile is white
        adj_count = len(adjacent & black_tiles)
        if adj_count == 2:
            return True

    return False


"""
PART 1
"""
for commands in input_data:
    flip_tile(parse_line(commands))

print('[AoC] Challenge 1')
print(f'Amount of black tiles: {len(black_tiles)}')
print()


"""
PART 2
"""
print('[AoC] Challenge 2')
for day in range(1, 101):
    to_flip = set()

    to_search = tiles_to_search()
    for tile in to_search:
        if should_flip(tile):
            to_flip.add(tile)

    for tile in to_flip:
        flip_tile(tile)

    if day % 10 == 0:
        print(f'Day {day}: {len(black_tiles)}')
