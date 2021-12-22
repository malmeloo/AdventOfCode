import aoc

input_data = aoc.get_input()


def _parse_line(line: str):
    status, cube = line.split(' ')

    turn_on = True if status == 'on' else False
    coords = tuple(tuple(int(e) for e in c.split('=')[-1].split('..')) for c in cube.split(','))

    return turn_on, coords


class Region:
    def __init__(self, x: tuple, y: tuple, z: tuple):
        self.x, self.y, self.z = x, y, z

    @property
    def size(self):
        return self.x[1] - self.x[0] + 1, self.y[1] - self.y[0] + 1, self.z[1] - self.z[0] + 1

    @property
    def volume(self):
        size = self.size
        return size[0] * size[1] * size[2]

    def __repr__(self):
        return f'Region(x={self.x}, y={self.y}, z={self.z})'

    def __bool__(self):
        return self.x != (0, 0) and self.y != (0, 0) and self.z != (0, 0)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def intersect(self, other: 'Region') -> 'Region':
        x_upper = min(other.x[1], self.x[1])
        x_lower = max(other.x[0], self.x[0])
        x_diff = max(x_upper - x_lower, 0)

        y_upper = min(other.y[1], self.y[1])
        y_lower = max(other.y[0], self.y[0])
        y_diff = max(y_upper - y_lower, 0)

        z_upper = min(other.z[1], self.z[1])
        z_lower = max(other.z[0], self.z[0])
        z_diff = max(z_upper - z_lower, 0)

        if x_diff <= 0 or y_diff <= 0 or z_diff <= 0:
            return Region((0, 0), (0, 0), (0, 0))

        return Region(
            (x_lower, x_upper),
            (y_lower, y_upper),
            (z_lower, z_upper)
        )


def _added_volume(region: Region, compare_to: list[Region]):
    volume = region.volume
    to_subtract = set()
    for reg in compare_to:
        intersect = region.intersect(reg)
        if intersect:
            to_subtract.add(intersect)

    for sub in to_subtract:
        volume -= _added_volume(sub, list(to_subtract - {sub}))

    return volume


class CubeManager:
    def __init__(self):
        self.enabled_regions: set[Region] = set()
        self.disabled_regions: set[Region] = set()

        self.cube_count = 0

    def add_region(self, region: Region):
        volume = region.volume
        intersects = []

        # first, remove all intersections with other cubes
        # so that we don't enable cubes twice
        for other_region in self.enabled_regions:
            intersect = region.intersect(other_region)
            if intersect:
                volume -= intersect.volume
                intersects.append(other_region)

        # intersections can overlap with each other,
        # in which case we removed too much.
        sign = 1
        while intersects:
            intersected = False
            new_intersects = []
            for i, inter1 in enumerate(intersects):
                for inter2 in intersects[i + 1:]:
                    intersect = inter1.intersect(inter2)
                    if intersect:
                        main_intersect = intersect.intersect(region)
                        intersected = True
                        new_intersects.append(main_intersect)
                        volume += main_intersect.volume * sign

            if not intersected:
                break

            intersects = new_intersects.copy()
            sign *= -1

        self.cube_count += volume
        self.enabled_regions.add(region)


def _clamp(num, _min, _max):
    return min(max(num, _min), _max)


def challenge1():
    grid_coords = set()

    for line in input_data:
        enable, coords = _parse_line(line)

        x_range = sorted((
            _clamp(coords[0][0], -50, 50),
            _clamp(coords[0][1], -50, 50) + 1,
        ))
        y_range = sorted((
            _clamp(coords[1][0], -50, 50),
            _clamp(coords[1][1], -50, 50) + 1,
        ))
        z_range = sorted((
            _clamp(coords[2][0], -50, 50),
            _clamp(coords[2][1], -50, 50) + 1,
        ))

        if any(ran[1] - ran[0] == 1 for ran in (x_range, y_range, z_range)):
            continue

        for x in range(*x_range):
            for y in range(*y_range):
                for z in range(*z_range):
                    if enable:
                        grid_coords.add((x, y, z))
                    else:
                        try:
                            grid_coords.remove((x, y, z))
                        except KeyError:
                            pass

    return len(grid_coords)


def challenge2():
    regions = []
    cube_count = 0

    for i, line in enumerate(input_data):
        on, region_data = _parse_line(line)
        region = Region(*region_data)
        if on:
            cube_count += _added_volume(region, regions)
            regions.append(region)
        else:
            added_vol = _added_volume(region, regions)
            removed_vol = region.volume - added_vol
            cube_count -= removed_vol

        print(f'{i + 1}/{len(input_data)} - {region}')

    return cube_count


# aoc.run(challenge1)
aoc.run(challenge2)
