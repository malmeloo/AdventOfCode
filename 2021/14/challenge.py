import copy
from typing import Generator, Iterable
import aoc

input_data = aoc.get_example()

template = list(input_data[0])
ins_rules = {a: b for (a, b) in [t.split(' -> ') for t in input_data[1:]]}


def _step(polymer: Generator[str, None, None]):
    last_elem = next(polymer)
    yield last_elem
    for elem in polymer:
        pair = last_elem + elem
        ins_elem = ins_rules.get(pair, None)
        if ins_elem is not None:
            yield ins_elem
        last_elem = elem
        yield elem


def _count_elem(polymer: Iterable):
    res = {}
    for elem in polymer:
        res[elem] = res.get(elem, 0) + 1

    return res


def challenge1():
    res = (i for i in copy.copy(template))

    gen = _step(res)
    for i in range(10 - 1):
        gen = _step(gen)

    count = _count_elem(gen)
    return max(count.values()) - min(count.values())


def challenge2():
    res = (i for i in copy.copy(template))

    gen = _step(res)
    for i in range(40 - 1):
        gen = _step(gen)

    count = _count_elem(gen)
    return max(count.values()) - min(count.values())


aoc.run(challenge1)
aoc.run(challenge2)
