import pytest
from kapusta_math.evaluation import evaluate


def test_basic_eval():
    assert evaluate("2+2") == 4
    assert evaluate("2*3") == 6
    assert evaluate("1+2*3") == 7
    assert evaluate("(1+2)*3") == 9
    assert evaluate("4+2/2") == 5
    assert evaluate("(4+2)/2") == 3

    assert evaluate("(1*3*(2+2))/6+2") == 4
    assert evaluate("(1*3*2+3)/6+2") == 3.5

    with pytest.raises(SyntaxError):
        evaluate("*3")
    with pytest.raises(SyntaxError):
        evaluate("(1*3")
