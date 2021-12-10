import aoc

input_data = aoc.get_input()
to_remove = set()

char_lookup = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
char_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
missing_char_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


class IllegalCharException(Exception):
    def __init__(self, *args, char=None):
        super().__init__(*args)

        self.char = char


class MissingCharException(Exception):
    def __init__(self, *args, chars=None):
        super().__init__(*args)

        self.chars = chars


def _parse_line(line: str):
    last_chars = []
    for char in line:
        if char in char_lookup.keys():
            last_chars.append(char)
        elif char in char_lookup.values():
            last_char = last_chars.pop(-1)
            if char != char_lookup[last_char]:
                raise IllegalCharException(char=char)

    if last_chars:
        raise MissingCharException(chars=last_chars)


def challenge1():
    score = 0
    for i, line in enumerate(input_data):
        try:
            _parse_line(line)
        except IllegalCharException as e:
            score += char_scores[e.char]
            to_remove.add(i)
        except MissingCharException:
            pass

    return score


def challenge2():
    scores = []
    for i, line in enumerate(input_data):
        if i in to_remove:
            continue

        try:
            _parse_line(line)
        except MissingCharException as e:
            missing_chars = [char_lookup[char] for char in reversed(e.chars)]
            score = 0
            for char in missing_chars:
                score = score * 5 + missing_char_scores[char]

            scores.append(score)

    scores = sorted(scores)

    return scores[len(scores) // 2]


aoc.run(challenge1)
aoc.run(challenge2)
