from advent_of_code import get_input

YEAR = '2022'


def day_1():
    _input = get_input(YEAR, '1')
    input_list = _input.split('\n')
    fattest_elf = 0
    current_elf = 0
    for i in input_list:
        if not i:
            if fattest_elf < current_elf:
                fattest_elf = current_elf
            current_elf = 0
        else:
            current_elf += int(i)
    return fattest_elf


if __name__ == '__main__':
    print(day_1())

