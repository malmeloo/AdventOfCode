import sys
from pathlib import Path

SCRIPT_PATH = Path(sys.argv[0])
SCRIPT_DIR = SCRIPT_PATH.parent

PUZZLE_DAY = SCRIPT_DIR.name
PUZZLE_YEAR = SCRIPT_DIR.parent.name

CHALLENGE_COUNT = 0
CHALLENGES = []


def get_input(delim='\n', data_type=str):
    with Path(SCRIPT_DIR, 'input.txt').open('r') as file:
        input_text = file.read()

    res = [data_type(line) for line in input_text.split(delim) if line]

    return res


def get_example(delim='\n', data_type=str):
    with Path(SCRIPT_DIR, 'example.txt').open('r') as file:
        input_text = file.read()

    res = [data_type(line) for line in input_text.split(delim) if line]

    return res


def run(callback, *args, **kwargs):
    global CHALLENGE_COUNT
    CHALLENGE_COUNT += 1

    print(f'--- Challenge {CHALLENGE_COUNT}')
    res = callback(*args, **kwargs)
    print(f'Output: {res}')
    print()

    return res


if not Path(SCRIPT_DIR, 'input.txt').is_file():
    print('[AoC] No input found! Please download the input first.')
    sys.exit(1)


print('-------- Advent of Code --------')
print(f'Solution for Dec {PUZZLE_DAY}, {PUZZLE_YEAR}')
print('--------------------------------')
print()
