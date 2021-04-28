"""@package docstring

Entry point of our calculator.

"""

import eel
from kapusta_math.evaluation import evaluate

if __name__ == '__main__':
    eel.init("kapusta_gui")
    eel.start("index.html", close_callback=lambda *args, **kwargs: exit(0), size=(100, 100))
