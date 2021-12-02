import aoc

input_data = aoc.get_input(data_type=int)


def challenge1():
    inc_counter = 0
    last_val = input_data[0]
    for val in input_data[1:]:
        if val > last_val:
            inc_counter += 1

        last_val = val

    return inc_counter


def challenge2():
    inc_counter = 0
    last_window = input_data[0:3]
    splits = [input_data[i:i+3] for i in range(len(input_data))]
    for split in splits:
        print(split)
        if sum(split) > sum(last_window):
            inc_counter += 1

        last_window = split

    return inc_counter


aoc.run(challenge1)
aoc.run(challenge2)
