import os

import pyautogui
import time
from PIL import Image
import threading
import keyboard


def get_color():
    pyautogui.screenshot('screen.jpg')
    x, y = pyautogui.position()
    img = Image.open('screen.jpg')  # Can be many different formats.
    pix = img.load()
    print(pix[x, y])  # Get the RGBA Value of the a pixel of an image
    os.remove('screen.jpg')


def show_color():
    pass


def loop():
    while True:
        get_color()
        time.sleep(1)


threading.Thread(target=loop, daemon=True).start()
keyboard.wait("Enter")
