import os
import eel

from command import *
from textrespone import *

def start():
    eel.init("UI")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
    