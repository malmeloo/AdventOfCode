import aoc
import copy

input_data = aoc.get_input('\n', data_type=lambda line: line.split('-'))


class Cave:
    def __init__(self, name, neighbors: set = None):
        self.name: str = name
        self.neighbors: set = neighbors or set()

    @property
    def is_large(self):
        return self.name.isupper()

    def connect(self, cave: 'Cave'):
        self.neighbors.add(cave)
        cave.neighbors.add(self)

    def __eq__(self, other):
        return isinstance(other, Cave) and other.name == self.name

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f'Cave(name={self.name})'

    def __hash__(self):
        return hash(self.name)


def _build_caves():
    caves = set()
    for cave1, cave2 in input_data:
        cave1_obj = Cave(cave1)
        if cave1_obj not in caves:
            caves.add(cave1_obj)
        else:
            cave1_obj = next(cave for cave in caves if cave.name == cave1)

        cave2_obj = Cave(cave2)
        if cave2_obj not in caves:
            caves.add(cave2_obj)
        else:
            cave2_obj = next(cave for cave in caves if cave.name == cave2)

        cave1_obj.connect(cave2_obj)

    return caves


def _cave_dfs(cave, visited_caves=None, to_visit_twice: Cave = None) -> list:
    visited = copy.copy(visited_caves or [])
    visited.append(cave)

    if cave.name == 'end':
        return [visited]

    paths = []
    for jump in cave.neighbors:
        visit_count = visited.count(jump)
        can_visit_again = visit_count < 2 and jump == to_visit_twice

        path = []
        if visit_count == 0 or jump.is_large:
            path = _cave_dfs(jump, visited, to_visit_twice)
        elif can_visit_again:
            path = _cave_dfs(jump, visited, to_visit_twice)

        paths.extend(path)

    return paths


def challenge1():
    caves = _build_caves()
    start_cave = next(cave for cave in caves if cave.name == 'start')
    paths = _cave_dfs(start_cave)

    return len(paths)


def challenge2():
    caves = _build_caves()
    start_cave = next(cave for cave in caves if cave.name == 'start')
    small_caves = [cave for cave in caves if not cave.is_large and cave.name not in ('start', 'end')]

    paths = _cave_dfs(start_cave)
    for cave in small_caves:
        paths.extend(_cave_dfs(start_cave, to_visit_twice=cave))

    paths = sorted(paths)

    counter = 1
    last_path = paths[0]
    for i, path in enumerate(paths[1:]):
        if paths[i - 1] != last_path:
            counter += 1
        last_path = path

    return counter


aoc.run(challenge1)
aoc.run(challenge2)
