import aoc
import copy

input_data = aoc.get_input()
bit_len = len(input_data)


def challenge1():
    set_bit_count = [0] * len(input_data[0])
    for bits in input_data:
        for i, bit in enumerate(bits):
            if bit == '1':
                set_bit_count[i] = set_bit_count[i] + 1

    gamma = 0
    epsilon = 0
    for i, bit_count in enumerate(reversed(set_bit_count)):
        if bit_count < bit_len / 2:  # 0 is more common
            epsilon += 2**i
        elif bit_count > bit_len / 2:  # 1 is more common
            gamma += 2**i

    return gamma * epsilon


def _most_common(in_data, i: int):
    bits = [int(bits[i]) for bits in in_data]
    if bits.count(0) > bits.count(1):
        return 0
    elif bits.count(1) > bits.count(0):
        return 1
    else:
        return None


def challenge2():
    input_copy = copy.copy(input_data)
    bit_i = 0
    while len(input_copy) > 1:
        most_common = _most_common(input_copy, bit_i)
        if most_common == 1 or most_common is None:
            input_copy = [bits for bits in input_copy if bits[bit_i] == '1']
        elif most_common == 0:
            input_copy = [bits for bits in input_copy if bits[bit_i] == '0']

        bit_i += 1
    oxygen = int(input_copy[0], 2)

    input_copy = copy.copy(input_data)
    bit_i = 0
    while len(input_copy) > 1:
        most_common = _most_common(input_copy, bit_i)
        if most_common == 1 or most_common is None:
            input_copy = [bits for bits in input_copy if bits[bit_i] == '0']
        elif most_common == 0:
            input_copy = [bits for bits in input_copy if bits[bit_i] == '1']

        bit_i += 1
    co2 = int(input_copy[0], 2)

    return oxygen * co2


aoc.run(challenge1)
aoc.run(challenge2)
