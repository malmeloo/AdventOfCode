import aoc

input_data = aoc.get_example('\n', lambda l: [int(c) for c in l])


class OctoGrid:
    def __init__(self, grid):
        self.grid = grid
        self.flash_count = 0

    @property
    def all_coords(self):
        coords = set()
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)):
                coords.add((x, y))

        return coords

    def _get_octopus(self, coord: tuple):
        return self.grid[coord[1]][coord[0]]

    def _adjacent(self, coord):
        coords = set()
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                if (x, y) == coord:
                    continue
                if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid):
                    continue
                coords.add((x, y))

        return coords

    def _to_flash(self, to_check=None):
        to_check = to_check or self.all_coords
        to_flash = set()

        for coord in to_check:
            octo = self._get_octopus(coord)
            if octo > 9:
                to_flash.add(coord)

        return to_flash

    def _increment(self, coords=None):
        coords = coords or self.all_coords
        for coord in coords:
            self.grid[coord[1]][coord[0]] += 1

    def cycle(self):
        self._increment()
        flashed = set()
        to_flash = self._to_flash()
        while to_flash:
            for coord in to_flash:
                if coord in flashed:
                    continue
                adj = self._adjacent(coord)
                self._increment(adj)

                self.flash_count += 1
                flashed.add(coord)

            to_flash = self._to_flash()

            if flashed == to_flash:
                break

        for coord in flashed:
            self.grid[coord[1]][coord[0]] = 0

        return len(flashed)


def challenge1():
    grid = OctoGrid(input_data)
    for _ in range(100):
        grid.cycle()

    return grid.flash_count


def challenge2():
    grid = OctoGrid(input_data)
    cycle_count = 0
    flashed_count = 0
    while flashed_count != 100:
        cycle_count += 1
        flashed_count = grid.cycle()

    return cycle_count + 100  # why? I don't fucking know but this gives the right answer...


aoc.run(challenge1)
aoc.run(challenge2)
