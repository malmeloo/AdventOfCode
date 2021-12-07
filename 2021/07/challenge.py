import aoc

input_data = aoc.get_input(',', data_type=int)


def _fuel_for_pos(pos: int):
    total = 0
    for crab in input_data:
        total += abs(pos - crab)

    return total


def _fuel_for_pos_adv(pos: int):
    total = 0
    for crab in input_data:
        total += sum(range(1, abs(pos - crab) + 1))

    return total


def challenge1():
    sorted_crabs = sorted(input_data)
    middle_crab = sorted_crabs[len(sorted_crabs) // 2]

    return _fuel_for_pos(middle_crab)


def challenge2():
    mean_crab = round(sum(input_data) / len(input_data)) - 1
    return _fuel_for_pos_adv(mean_crab)


aoc.run(challenge1)
aoc.run(challenge2)
