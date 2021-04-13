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
    return 0


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
    return 0


def sqrt(x):
    """
    Square root of a number

    Parameters:
        x:      Number for sqrt
    """
    return math.sqrt(x)


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
