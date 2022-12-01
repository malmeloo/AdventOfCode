import aoc
import copy

input_data = aoc.get_example()


class Amphipod:
    def __init__(self, kind, x, y):
        self.kind = kind
        self.energy_used = 0
        self.x = x
        self.y = y

    @property
    def location(self):
        return self.x, self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'Amphipod(kind={self.kind}, x={self.x}, y={self.y})'


class Burrow:
    HALLWAY = {
        (1, 1),
        (2, 1),
        (4, 1),
        (6, 1),
        (8, 1),
        (10, 1),
        (11, 1),
    }
    ROOMS = {
        'A': 3,
        'B': 5,
        'C': 7,
        'D': 9
    }
    ENERGY = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
    }

    def __init__(self):
        self._amphipods: set[Amphipod] = set()

    @property
    def active_amphipods(self):
        return {a for a in self._amphipods if not self.reached_room(a)}

    @property
    def energy_used(self):
        return sum(a.energy_used for a in self._amphipods)

    def add(self, amphipod: Amphipod):
        self._amphipods.add(amphipod)

    def print(self):
        pod_locations = {a.location: a.kind for a in self._amphipods}
        for y in range(0, 5):
            for x in range(0, 13):
                if (x, y) in pod_locations:
                    print(pod_locations[(x, y)], end='')
                elif x in range(1, 12) and y == 1 or x in range(3, 10, 2) and y in range(1, 4):
                    print('.', end='')
                else:
                    print('#', end='')
            print()
        print()

    def move(self, amphipod: Amphipod, x, y):
        energy = 0

        energy += abs(x - amphipod.x)  # for going left/right

        energy += amphipod.y - 1  # for going up
        energy += y - 1  # for going down

        amphipod.energy_used = energy * self.ENERGY[amphipod.kind]
        amphipod.x = x
        amphipod.y = y

    def find(self, x=None, y=None):
        if x and y:
            return {a for a in self._amphipods if a.location == (x, y)}
        elif x:
            return {a for a in self._amphipods if a.x == x}
        else:
            return {a for a in self._amphipods if a.y == y}

    def reached_room(self, amphipod: Amphipod):
        target_x = self.ROOMS[amphipod.kind]
        room_pods = self.find(x=target_x)

        if amphipod.x == target_x and amphipod.y == 3:  # bottom, so dest reached
            return True
        elif all(a.kind == amphipod.kind for a in room_pods):  # not bottom, but both reached target
            return True
        else:
            return False

    def _room_jump(self, amphipod: Amphipod):
        target_x = self.ROOMS[amphipod.kind]
        occupying_pods = self.find(x=target_x)
        if len(occupying_pods) == 0:  # room empty, so you can go there
            return {(target_x, 3)}
        elif len(occupying_pods) == 1 and next(iter(self.find(target_x, 3))).kind == amphipod.kind:
            return {(target_x, 2)}
        else:  # no place for you to go
            return set()

    def jump_locations(self, amphipod: Amphipod):
        taken_locations = {a.location for a in self._amphipods}
        if amphipod.x in self.ROOMS.values():  # amphipod in a room, must go into hallway
            if amphipod.y == 3 and (amphipod.x, amphipod.y - 1) in taken_locations:  # blocked exit
                return set()

            hallway_pods = self.find(y=1)
            left_pods = sorted([a for a in hallway_pods if a.x < amphipod.x], key=lambda a: a.x)
            right_pods = sorted([a for a in hallway_pods if a.x > amphipod.x], key=lambda a: a.x)

            bound = [1, 12]
            if left_pods:
                bound[0] = left_pods[-1].x + 1
            if right_pods:
                bound[1] = right_pods[0].x

            hallway_jumps = {(x, 1) for x in range(*bound) if (x, 1) in self.HALLWAY}
            room_jumps = self._room_jump(amphipod)

            return hallway_jumps | room_jumps
        else:  # amphipod in hallway, must go to room
            return self._room_jump(amphipod)


def _parse_burrow(burrow_lines):
    burrow = Burrow()

    for y, line in enumerate(burrow_lines):
        for x, char in enumerate(line):
            if char in ('A', 'B', 'C', 'D'):
                burrow.add(Amphipod(char, x, y))

    return burrow


def _lowest_energy(burrow):
    if not burrow.active_amphipods:
        return burrow.energy_used

    burrow.print()

    lowest_energy = 9999999999

    for a in burrow.active_amphipods:
        locations = burrow.jump_locations(a)
        for location in locations:
            new_burrow = copy.deepcopy(burrow)
            pod = next(iter(new_burrow.find(x=a.x, y=a.y)))
            new_burrow.move(pod, location[0], location[1])

            energy = _lowest_energy(new_burrow)
            if energy < lowest_energy:
                lowest_energy = energy

    return lowest_energy


def challenge1():
    burrow = _parse_burrow(input_data)

    return _lowest_energy(burrow)


aoc.run(challenge1)
