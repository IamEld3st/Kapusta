from kapusta_math.evaluation import evaluate


def test_basic_eval():
    assert evaluate("2+2") == 4
    assert evaluate("2*3") == 6