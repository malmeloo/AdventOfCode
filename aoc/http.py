from pathlib import Path

import requests

INPUT_URL = 'https://adventofcode.com/{year}/day/{day}/input'
LEADERBOARD_URL = 'https://adventofcode.com/{year}/leaderboard/private/view/{leaderboard_id}.json'


class InvalidCookieException(Exception):
    pass


def get_session_cookie(root_dir: Path):
    try:
        with Path(root_dir, '_session.txt').open('r') as file:
            cookie = file.read()
    except FileNotFoundError:
        return None

    return cookie.strip()


def download_input(cookie: str, year: int, day: int):
    r = requests.get(
        INPUT_URL.format(year=year, day=day),
        cookies={'session': cookie}
    )
    if r.status_code == 404:
        return None
    elif r.status_code == 500:
        raise InvalidCookieException

    r.raise_for_status()

    return r.text


def download_leaderboard(cookie: str, year: int, lb_id: int):
    r = requests.get(
        LEADERBOARD_URL.format(year=year, leaderboard_id=lb_id),
        cookies={'session': cookie}
    )
    if r.status_code == 404:
        return None
    elif r.status_code == 500:
        raise InvalidCookieException

    r.raise_for_status()

    return r.json()
