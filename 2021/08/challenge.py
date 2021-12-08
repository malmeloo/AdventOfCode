import itertools

import aoc

input_data = aoc.get_input()
normal_layout = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


"""
strategy:
- 1, 4, 7 and 8 are easy to spot
left: 0, 2, 3, 5, 6, 9

- 0 is the only one without d
left: 2, 3, 5, 6, 9

- 9 is a subset of 4
left: 2, 3, 5, 6

- 6 is the only one with 6 segments
left: 2, 3, 5

- 3 is a subset of 1
left: 2, 5

- the difference between 5 and 6 is one segment
left: none
"""


def challenge1():
    res = 0
    for line in input_data:
        patterns, output_values = line.split(' | ')
        for value in output_values.split(' '):
            if len(value) in (2, 4, 3, 7):
                res += 1

    return res


def _find_first_4(patterns):
    num_len = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    out = {}

    for pattern in patterns:
        if len(pattern) in num_len.keys():
            out[pattern] = num_len[len(pattern)]

    return out


def _find_0(patterns):
    segment_count = {}
    for pattern in patterns:
        for char in pattern:

            segment_count[char] = segment_count.get(char, 0) + 1

    print(segment_count)


def challenge2():
    res = 0
    for line in input_data:
        split = line.split(' | ')
        patterns = split[0].split(' ')
        output_values = split[1].split(' ')

        perms = itertools.permutations('abcdefg')
        for perm in perms:
            trans = str.maketrans('abcdefg', ''.join(perm))
            pat_trans = [''.join(sorted(code.translate(trans))) for code in patterns]
            val_trans = [''.join(sorted(code.translate(trans))) for code in output_values]

            # todo: replace with all()
            found = True
            for code in pat_trans:
                if code not in normal_layout:
                    found = False

            if found:
                code_str = ''
                for code in val_trans:
                    code_str += str(normal_layout[code])

                res += int(''.join(code_str))

    return res


aoc.run(challenge1)
aoc.run(challenge2)
