import pytest

from advent_of_code.y2022 import day_2


def test_day_2():
    test_data = 'A Y\nB X\nC Z'
    result_1, result_2 = day_2(test_data)
    assert result_2 == 15
