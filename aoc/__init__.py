import sys
from pathlib import Path
import requests

from . import http

SCRIPT_PATH = Path(sys.argv[0])
SCRIPT_DIR = SCRIPT_PATH.parent
ROOT_DIR = SCRIPT_DIR.parent.parent

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
    session_cookie = http.get_session_cookie(ROOT_DIR)
    if session_cookie is None:
        print('[AoC] No input found! Please download the input first, or put your session cookie in '
              '_session.txt to download the input automatically.')
        sys.exit(1)

    print('[AoC] Automatically downloading input data...')

    try:
        input_data = http.download_input(session_cookie, int(PUZZLE_YEAR), int(PUZZLE_DAY))
    except http.InvalidCookieException:
        print('[AoC] Invalid cookie in _session.txt. Try entering it again.')
        sys.exit(1)

    if input_data is None:
        print('[AoC] Puzzle has not yet been unlocked. Nice try!')
        sys.exit(1)

    with Path(SCRIPT_DIR, 'input.txt').open('w+') as file:
        file.write(input_data)

    print('[AoC] Successfully downloaded input data.')
    print()


print('-------- Advent of Code --------')
print(f'Solution for Dec {PUZZLE_DAY}, {PUZZLE_YEAR}')
print('--------------------------------')
print()
