import argparse
from advent_of_code import y2022
parser = argparse.ArgumentParser(
    prog='Advent Of Code Solutions',
    description='Oliver\'s Advent Of Code Solutions',
)
parser.add_argument('year')
parser.add_argument('day')

args = parser.parse_args()
print(f'executing day {args.day} of year {args.year}')
result_1, result_2 = y2022.execute_day(args.day)
print(f'executed day {args.day} of year {args.year}. part 1 result ={result_1} | part 2 result ={result_2}')

