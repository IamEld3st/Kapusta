"""@package operations

Module for math operations.

Each function of this module is called by evaluation.evaluation().

"""

import math


def add(a, b):
    """
    Sum of two numbers

    Parameters:
        a:      first number
        b:      second number
    """
    return a + b


def sub(a, b):
    """
    Substract a number from a different number

    Parameters:
        a:      Substracted number
        b:      Amount to substract
    """
    return a - b


def mul(a, b):
    """
    Multiplication of 2 numbers

    Parameters:
        a:      First number to multiply
        b:      Second number to multiply
    """
    return a * b


def div(a, b) -> float:
    """
    Divide a number by number

    Parameters:
        a: Number to divide (dividend)
        b: Number to divide with (divisor)
    """
    if b == 0:
        raise ZeroDivisionError

    return a / b


def sin(x):
    """
    The sine of a number

    Parameters:
        x:      Number for sin (should be in radians)
    """
    return math.sin(x)


def root(n, x=-1):
    if x == -1:
        x = 2
        n, x = x, n

    """
    Root-n of a number

    Parameters:
        x:      Number for sqrt
        n:      Nth root
    """
    if x < 0 or n < 1:
        raise ValueError

    return x**(1/float(n))


def pwr(x, y):
    """
    The power of a number

    Parameters:
        x:      The base
        y:      The exponent
    """
    return x**y


def fac(x):
    """
    Factorial of a number

    Parameters:
        x:      Number for factorial
    """
    if x == 0:
        return 1
    if x < 0:
        raise ValueError

    return x*fac(x-1)
