"""@package evaluation

Module for evaluate() function.

Module used for evaluating provided expression.
Defined global variables (BOTH_SIDES, LEFT_SIDE, RIGHT_SIDE) are used to determine, where operands are.

"""


import eel
from kapusta_math.operations import *
import re


def _check_syntax(eval_str):
    if eval_str.count("(") != eval_str.count(")"):
        raise SyntaxError("Invalid expression")


NUMBER = r"([-]?(?:[0-9]*[.,])?[0-9]+)"
# side of value(s)
BOTH_SIDES = fr"{NUMBER}...{NUMBER}"
LEFT_SIDE = fr"{NUMBER}..."
RIGHT_SIDE = fr"...{NUMBER}"
ROOT_OPERATION = fr"{NUMBER}√{NUMBER}|√{NUMBER}"


@eel.expose
def evaluate(eval_str):
    """
        Evaluates provided string.
        Function is able to compute expression containing parentheses in proper order.

        Parameters:
            eval_str: expression to solve
    """
    _check_syntax(eval_str)

    if "(" in eval_str:  # solve parentheses
        expression_start = eval_str.find("(") + 1  # +1 to move behind (, so only content is processed
        expression_end = eval_str.rfind(")")
        result = evaluate(eval_str[expression_start:expression_end])  # solve problem in parentheses

        eval_str = f"{result}".join((eval_str[:expression_start-1], eval_str[expression_end+1:]))  # replace parentheses with result

    # operations sorted by priority, ("operator", function, side_of_values)
    # regex special characters have to be escaped
    operations = [
        [(r"\^", pwr, BOTH_SIDES), (r"\!", fac, LEFT_SIDE), (r"√", root, ROOT_OPERATION), (r"sin", sin, RIGHT_SIDE)],
        [(r"\*", mul, BOTH_SIDES), (r"\/", div, BOTH_SIDES)],
        [(r"\+", add, BOTH_SIDES), (r"\-", sub, BOTH_SIDES)]]

    for priority in operations:
        for operator in priority:
            operator, operation, pattern = operator
            pattern = pattern.replace("...", operator)

            while True:  # replacing until all operation's results are calculated (inc. intermediate results)
                replaced = re.sub(pattern, lambda x: str(operation(*(float(number) for number in x.groups() if number))), eval_str)
                #                                     ^ sub() supports strings only         ^ skipping empty groups
                if replaced == eval_str:
                    break
                eval_str = replaced

    try:
        result = float(eval_str)
    except ValueError:
        raise SyntaxError("Invalid expression")

    return result
