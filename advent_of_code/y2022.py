from typing import List

from advent_of_code import get_input

YEAR = '2022'


def execute_day(day):
    data = get_input(YEAR, day)
    if day == '1':
        return day_1(data)
    if day == '2':
        return day_2(data)


def day_1(data):
    input_list = data.split('\n')
    elf_calorie_totals = [0]
    for i in input_list:
        if not i:
            elf_calorie_totals.append(0)
        else:
            elf_calorie_totals[-1] += int(i)
    elf_calorie_totals = sorted(elf_calorie_totals, reverse=True)
    return elf_calorie_totals[0], sum(elf_calorie_totals[0:3])


def day_2(data: str):
    data = data.replace('A', '1')
    data = data.replace('B', '2')
    data = data.replace('C', '3')
    data = data.replace('X', '1')
    data = data.replace('Y', '2')
    data = data.replace('Z', '3')
    data = data.strip()
    input_list = data.split('\n')

    elf_total = 0
    santa_total = 0
    for match in input_list:
        elf = int(match[0])
        santa = int(match[2])

        if elf == santa:
            elf += 3
            santa += 3
        elif santa > 1 and elf == santa - 1:
            santa += 6
        elif santa == 1 and elf == 3:
            santa += 6
        else:
            elf += 6
        #  santa 1 and elf 3 | santa 2 and elf 1 | santa 3 and elf 2
        elf_total += elf
        santa_total += santa

    return elf_total, santa_total


def day_2_part_2(data: str):
    data = data.strip()
    input_list = data.split('\n')
    new_input = ''
    for index, match in enumerate(input_list):
        elf = match[0]
        result = match[2]
        if elf == 'A':

