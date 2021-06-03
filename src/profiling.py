#!/usr/bin/python
# -*- coding: utf-8 -*-

"""@package docstring

Script used to calculate standard deviation using our math library.

"""

import sys
from kapusta_math.operations import *


def deviation(numbers: list[float]) -> float:
    """
    Variance of numbers.

    Parameters:
        numbers:    the numbers to calculate variance from
    """
    no_of_numbers = len(numbers)

    sum_x = 0
    for x in numbers:
        sum_x = add(sum_x, x)

    xx = mul(div(1, no_of_numbers), sum_x)

    sum_xx_pwr = 0
    for x in numbers:
        sum_xx_pwr = add(sum_xx_pwr, pwr(x, 2))

    to_sqrt = mul(div(1, sub(no_of_numbers, 1)), sub(sum_xx_pwr, mul(no_of_numbers, pwr(xx, 2))))

    s = root(to_sqrt)
    return s


def load_numbers() -> list[float]:
    """
    Function loads numbers for variance().
    """
    numbers = sys.stdin.read().strip().split()
    int_numbers = []

    for number in numbers:
        try:
            int_numbers.append(float(number))
        except ValueError:
            print("Invalid number sequence!", file=sys.stderr)
            exit(1)

    return int_numbers


if __name__ == "__main__":
    print(deviation(load_numbers()))
