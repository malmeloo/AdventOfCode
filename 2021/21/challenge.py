import aoc
import functools

input_data = aoc.get_input('\n', data_type=lambda l: int(l.split(': ')[-1]))


class DeterministicDie:
    def __init__(self):
        self.roll_count = 0
        self.i = 0

    def __iter__(self):
        return self

    def roll(self):
        res = 0
        for _ in range(3):
            res += next(self)

        return res

    def __next__(self):
        self.roll_count += 1
        self.i += 1
        if self.i > 100:
            self.i = 1

        return self.i


class Player:
    def __init__(self, pos, target_score):
        self.score = 0
        self.pos = pos
        self.target_score = target_score

    def __lt__(self, other):
        return isinstance(other, Player) and self.score < other.score

    @property
    def has_won(self):
        return self.score >= self.target_score

    def move(self, spaces):
        self.pos = (self.pos + spaces) % 10
        if self.pos == 0:
            self.pos = 10

        self.score += self.pos


def challenge1():
    players = [Player(score, 1000) for score in input_data]
    die = DeterministicDie()

    while not any(p.has_won for p in players):
        spaces = die.roll()
        players[0].move(spaces)

        # reverse turn
        players = [players[1], players[0]]

    return min(players).score * die.roll_count


# possible steps ahead for every move (3 dice throws)
dirac_sums = {}
for i1 in range(1, 4):
    for i2 in range(1, 4):
        for i3 in range(1, 4):
            s = i1 + i2 + i3
            dirac_sums[s] = dirac_sums.get(s, 0) + 1


@functools.cache
def _dirac_die(p1_pos, p1_score, p2_pos, p2_score):
    if p1_score > 20:
        return 1, 0
    if p2_score > 20:
        return 0, 1

    final_p1_wins = 0
    final_p2_wins = 0
    for dirac_sum, count in dirac_sums.items():
        # move and calculate new score
        new_p1_pos = (p1_pos + dirac_sum) % 10
        if new_p1_pos == 0:
            new_p1_pos = 10
        new_p1_score = p1_score + new_p1_pos

        # swap players around so we can calculate for p2
        p2_wins, p1_wins = _dirac_die(p2_pos, p2_score, new_p1_pos, new_p1_score)

        final_p1_wins += p1_wins * count
        final_p2_wins += p2_wins * count

    return final_p1_wins, final_p2_wins


def challenge2():
    res = _dirac_die(input_data[0], 0, input_data[1], 0)
    return max(res)


aoc.run(challenge1)
aoc.run(challenge2)
