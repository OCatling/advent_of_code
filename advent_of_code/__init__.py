import os
import requests

CACHE_DIR = os.path.join(os.getcwd(), '.cache')
URL = 'https://adventofcode.com/'
SESSION_ID = os.getenv('AOC_SESSION_ID')


def get_input(year: str, day: str):
    cache_dir = os.path.join(CACHE_DIR, year)
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    cached_input_path = os.path.join(cache_dir, f'input_day_{day}')
    if os.path.exists(cached_input_path):
        with open(cached_input_path, 'r') as in_file:
            return in_file.read()

    url = f'{URL}{year}/day/{1}/input'
    resp = requests.get(url, cookies={'session': SESSION_ID})
    with open(cached_input_path, 'w') as out_file:
        out_file.write(resp.text)
        return resp.text
