from pathlib import Path
import sys

from aoc import http

session_cookie = http.get_session_cookie(Path('.'))
if session_cookie is None:
    print('[AoC] No session cookie found! Please put it in _session.txt')
    sys.exit(1)


def parse_leaderboard(lb: dict):
    star_deltas = {}

    for user, userdata in lb['members'].items():
        for star, stardata in userdata['completion_day_level'].items():
            if '2' not in stardata:  # not completed yet
                continue

            ts1 = int(stardata['1']['get_star_ts'])
            ts2 = int(stardata['2']['get_star_ts'])
            delta = ts2 - ts1

            new_data = star_deltas.get(int(star), [])
            new_data.append({
                'id': userdata['id'],
                'name': userdata['name'] or 'unknown',
                'delta': delta
            })
            star_deltas[int(star)] = new_data

    return star_deltas


def _fmt_user(user: dict, avg):
    delta_dist = round(user.get('delta') - avg)
    return f'{user["name"]:<30} {user["delta"]:<15} {delta_dist}'


def main():
    print('[AoC] Enter year:')
    year = int(input('> '))
    print('[AoC] Enter leaderboard ID:')
    lb_id = int(input('> '))

    try:
        leaderboard = http.download_leaderboard(session_cookie, year, lb_id)
    except http.InvalidCookieException:
        print('[AoC] Invalid cookie in _session.txt. Try entering it again.')
        sys.exit(1)

    if leaderboard is None:
        print('[AoC] Could not find leaderboard!')
        sys.exit(1)
    print()

    parsed = parse_leaderboard(leaderboard)
    for day in sorted(parsed.keys()):
        all_deltas = [user.get('delta') for user in parsed[day]]
        avg_delta = sum(all_deltas) / len(all_deltas)
        delta_lb = sorted(parsed[day], key=lambda user: user.get('delta'))

        print(f'--- Day: {day} (delta average: {round(avg_delta)})')
        print('User name                          Star delta      Dist from average')
        print(f'1 - {_fmt_user(delta_lb[0], avg_delta)}')
        print(f'2 - {_fmt_user(delta_lb[1], avg_delta)}')
        print(f'3 - {_fmt_user(delta_lb[2], avg_delta)}')

        print()


if __name__ == '__main__':
    sys.exit(main())
