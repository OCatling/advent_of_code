from typing import List

from advent_of_code import get_input

YEAR = '2022'


def execute_day(day):
    input_ = get_input(YEAR, day)
    if day == '1':
        return day_1(input_)


def day_1(input_):
    input_list = input_.split('\n')
    elf_calorie_totals = [0]
    for i in input_list:
        if not i:
            elf_calorie_totals.append(0)
        else:
            elf_calorie_totals[-1] += int(i)
    elf_calorie_totals = sorted(elf_calorie_totals, reverse=True)
    return elf_calorie_totals[0], sum(elf_calorie_totals[0:3])
