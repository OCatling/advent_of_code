from typing import List

from advent_of_code import get_input

YEAR = '2022'


def execute_day(day):
    data = get_input(YEAR, day)
    data = data.strip()
    data = data.split('\n')
    if day == '1':
        return day_1(data)
    if day == '2':
        _, part_1_result = day_2(data)
        data = day_2_part_2(data)
        _, part_2_result = day_2(data)
        return part_1_result, part_2_result
    if day == '3':
        return day_3(data)


def day_1(data: List[str]):
    elf_calorie_totals = [0]
    for i in data:
        if not i:
            elf_calorie_totals.append(0)
        else:
            elf_calorie_totals[-1] += int(i)
    elf_calorie_totals = sorted(elf_calorie_totals, reverse=True)
    return elf_calorie_totals[0], sum(elf_calorie_totals[0:3])


def day_2(data: List[str]):
    def sanitize(string: str):
        string = string.replace('A', '1')
        string = string.replace('B', '2')
        string = string.replace('C', '3')
        string = string.replace('X', '1')
        string = string.replace('Y', '2')
        string = string.replace('Z', '3')
        return string
    data = [sanitize(i) for i in data]

    elf_total = 0
    santa_total = 0
    for match in data:
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
        elf_total += elf
        santa_total += santa

    return elf_total, santa_total


def day_2_part_2(data: List[str]):
    new_input = []
    for match in data:
        elf = match[0]
        if elf == 'A':
            match = match.replace('X', 'C')
            match = match.replace('Y', 'A')
            match = match.replace('Z', 'B')
        elif elf == 'B':
            match = match.replace('X', 'A')
            match = match.replace('Y', 'B')
            match = match.replace('Z', 'C')
        elif elf == 'C':
            match = match.replace('X', 'B')
            match = match.replace('Y', 'C')
            match = match.replace('Z', 'A')
        new_input.append(f'{match}\n')
    return new_input


def day_3(data: List[str]):
    import string

    def sanitize(input_string: str):
        letters = list(string.ascii_lowercase + string.ascii_uppercase)
        for index, letter in enumerate(letters):
            input_string = input_string.replace(letter, f'{index + 1},')
        input_string = input_string[:-1]
        return input_string
    data = [sanitize(i) for i in data]

    total = 0
    for backpack in data:
        backpack = backpack.strip()
        backpack = backpack.split(',')
        backpack = [int(i) for i in backpack]
        first_compartment = sorted(backpack[len(backpack) // 2:])
        second_compartment = sorted(backpack[:len(backpack) // 2])
        main_item = set(first_compartment) & set(second_compartment)
        total += main_item.pop()
    return total, None
