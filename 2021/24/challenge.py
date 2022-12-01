import aoc
import difflib

input_data = aoc.get_input()


def challenge1():
    """
    This just simplifies the input for manual parsing.
    All "chunks" separated by inp are 18 lines long, so
    we can compare the differences.
    """
    chunks = []
    digit_chunk = []
    for line in input_data:
        if line.startswith('inp') and digit_chunk:
            chunks.append(digit_chunk)
            digit_chunk = []

        digit_chunk.append(line)

    for i in range(len(chunks[0])):
        normal = chunks[0][i]
        print(normal, end='')
        for other in chunks[1:]:
            other_str = other[i]
            if other_str != normal:
                print(f' - {other_str}', end='')
        print()


def the_code():
    """
    We can pick any digit, as long as it is not equal to whatever x is.
    Due to the way this algo works, z is always increased.
    """
    digit = 1

    result = 0
    x = 14  # (OR 13, 12, -7 ...)

    # x can be any digit, but it must NOT be equal to
    if x != digit:
        x = 0
        y = 1
    else:
        x = 1
        y = 26

    result = result * y + (digit + 12) * x  # always positive constant


aoc.run(challenge1)
