import os
import sys
import platform
import eel
from kapusta_math.evaluation import evaluate

if __name__ == '__main__':
    gui_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'kapusta_gui')
    eel.init(gui_folder)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        pltf = platform.system()
        if pltf == "Linux":
            electron_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromium/chrome')
        else:
            electron_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromium/chrome.exe')
        eel.browsers.set_path('chrome', electron_folder)
    eel.start("index.html", mode="chrome", size=(325,425))
