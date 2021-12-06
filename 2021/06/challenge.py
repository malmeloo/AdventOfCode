import aoc
import copy

input_data = aoc.get_input(',', data_type=int)


def challenge(loop_count):
    fishes = copy.copy(input_data)
    fish_count = {}
    for fish in fishes:
        fish_count[fish] = fish_count.get(fish, 0) + 1

    for _ in range(loop_count):
        # verbose as fuck lmao
        fish_count = {
            0: fish_count.get(1, 0),
            1: fish_count.get(2, 0),
            2: fish_count.get(3, 0),
            3: fish_count.get(4, 0),
            4: fish_count.get(5, 0),
            5: fish_count.get(6, 0),
            6: fish_count.get(7, 0) + fish_count.get(0, 0),
            7: fish_count.get(8, 0),
            8: fish_count.get(0, 0)
        }

    return sum(fish_count.values())


aoc.run(lambda: challenge(80))
aoc.run(lambda: challenge(256))
