import aoc

cups = [int(c) for c in list(aoc.get_example()[0])]

lowest_cup = min(cups)
highest_cup = max(cups)


def pickup_cups(index, count):
    to_pickup = []
    for i in range(0, count):
        to_pickup.append(cups[(index + i) % len(cups)])

    for cup in to_pickup:
        cups.remove(cup)

    return to_pickup


def find_dest(current):
    to_insert = current
    while True:
        to_insert -= 1
        if to_insert in cups:
            return to_insert
        elif to_insert < lowest_cup:
            to_insert = highest_cup


"""
Part 1
"""
print()

cur_cup = (0, cups[0])
for move in range(1, 11):
    print(f'-- move {move} --')

    cup_list = [str(c) for c in cups]
    print(f'cups: {" ".join(cup_list)}')

    print(f'cur cup: {cur_cup[1]}')

    pickup = pickup_cups(cur_cup[0] + 1, 3)
    pickup_list = [str(c) for c in pickup]
    print(f'pick up: {", ".join(pickup_list)}')

    dest = find_dest(cur_cup[1])
    dest_index = cups.index(dest) + 1
    print(f'destination: {dest}')
    print()

    cups = cups[:dest_index] + pickup + cups[dest_index:]

    new_cur_cup_i = (cur_cup[0] + 1) % (len(cups) - 1)
    cur_cup = (new_cur_cup_i, cups[new_cur_cup_i])
