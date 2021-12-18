import copy
import json
import math

import aoc

input_data = aoc.get_input('\n', data_type=json.loads)


def _look_ahead(string, start_pos, lookup_char=None):
    for i, char in enumerate(string[start_pos:]):
        if char.isnumeric() and lookup_char is None or char == lookup_char:
            return start_pos + i

    return 0


def _get_num(string, start_pos):
    res = ''
    for char in string[start_pos:]:
        if not char.isnumeric():
            break

        res += char

    return int(res)


def _explode(num):
    num_str = json.dumps(num)

    last_num_i = 0
    nest_count = 0
    for i, char in enumerate(num_str):
        if char.isnumeric() and not num_str[i - 1].isnumeric():
            last_num_i = i

        if char == '[':
            nest_count += 1
        elif char == ']':
            nest_count -= 1

        if nest_count == 5:  # do explode here
            closing_i = _look_ahead(num_str, i, ']')
            left, right = json.loads(num_str[i:closing_i + 1])
            next_num_i = _look_ahead(num_str, closing_i + 1)

            # order is important to make sure indices work properly (string length may change)
            if next_num_i != 0:  # process right number
                old_num = _get_num(num_str, next_num_i)
                end_i = next_num_i + len(str(old_num))
                num_str = num_str[:next_num_i] + str(old_num + right) + num_str[end_i:]
            # replace pair by 0
            num_str = num_str[:i] + '0' + num_str[closing_i + 1:]
            if last_num_i != 0:  # process left number
                old_num = _get_num(num_str, last_num_i)
                end_i = last_num_i + len(str(old_num))
                num_str = num_str[:last_num_i] + str(old_num + left) + num_str[end_i:]

            break
    return json.loads(num_str)


def _split(num):
    if isinstance(num, int):
        if num >= 10:
            num = [math.floor(num / 2), math.ceil(num / 2)]
        return num

    left = _split(num[0])
    if left != num[0]:  # some change occurred, we can only make one modification at a time
        return [left, num[1]]

    right = _split(num[1])
    if right != num[1]:  # some change occurred, we can only make one modification at a time
        return [num[0], right]

    return [left, right]


def _add(num1, num2):
    pair = [num1, num2]

    while True:
        last_num = copy.deepcopy(pair)
        pair = _explode(pair)
        if pair != last_num:  # change occurred, go back
            continue

        last_num = copy.deepcopy(pair)
        pair = _split(last_num)
        if pair != last_num:  # change occurred, go back
            continue

        return pair


def _magnitude(num):
    if isinstance(num, int):
        return num
    left = _magnitude(num[0])
    right = _magnitude(num[1])

    return 3 * left + 2 * right


def challenge1():
    res = input_data[0]
    for num in input_data[1:]:
        res = _add(res, num)

    return _magnitude(res)


def challenge2():
    largest = 0
    for first in input_data:
        for second in input_data:
            if first == second:
                continue

            res = _add(first, second)
            mag = _magnitude(res)
            if mag > largest:
                largest = mag

    return largest


aoc.run(challenge1)
aoc.run(challenge2)
