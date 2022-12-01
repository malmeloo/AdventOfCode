import aoc

input_data = aoc.get_example(
    '\n\n',
    data_type=lambda l: [tuple(int(num) for num in beacon.split(',')) for beacon in l.splitlines()[1:]]
)


def _beacon_distances(scanner_data) -> list[set[tuple]]:
    distances = []
    for scanner in scanner_data:
        beacon_dist = set()
        for i, beacon1 in enumerate(scanner):
            for beacon2 in scanner[i + 1:]:
                diff = (
                    abs(beacon1[0] - beacon2[0]),
                    abs(beacon1[1] - beacon2[1]),
                    abs(beacon1[2] - beacon2[2])
                )
                beacon_dist.add(diff)

        distances.append(beacon_dist)

    return distances


def _beacon_count(link_count: int):
    d = (1 + 8 * link_count) ** 0.5
    res = (1 + d) / 2

    return int(res)


def challenge1():
    distances = _beacon_distances(input_data)

    for i1, scanner1 in enumerate(distances):
        for i2, scanner2 in enumerate(distances[i1 + 1:]):
            shared_links = len(scanner1 & scanner2)
            beacons = _beacon_count(shared_links)

            print(i1, i1 + i2)
            if beacons >= 12:
                print(beacons)


aoc.run(challenge1)
