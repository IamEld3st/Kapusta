import pytest
from kapusta_math.operations import *


def test_add():
    assert add(1, 2) == 3
    assert add(-3, 4) == 1
    assert add(-2, -2) != 4


def test_sub():
    assert sub(1, 2) == -1
    assert sub(-1, 1) == -2
    assert sub(1, 1) != 1


def test_mul():
    assert mul(1, 1) == 1
    assert mul(-2, 2) == -4
    assert mul(0, 42) != 42


def test_div():
    assert div(1, 2) == 0.5
    assert div(-1, 1) == -1
    assert div(1, 1) != 0
    with pytest.raises(ZeroDivisionError):
        div(69, 0)


def test_sin():
    assert sin(90) == 1
    assert sin(30) == 0.5
    assert sin(-180) == 0
    assert sin(70) > 0.9


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    with pytest.raises(ValueError):
        sqrt(-4)


def test_pow():
    assert pwr(1, 1) == 1
    assert pwr(2, 2) == 4
    assert pwr(-4, -2) == 1/16


def test_fac():
    assert fac(2) == 2
    assert fac(0) == 1
    assert fac(3) == 6
    with pytest.raises(ValueError):
        fac(-4)

