import time
from time import sleep
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


TOGGLE_KEY = KeyCode(char="k")
DELAY = 1.5

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(DELAY)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

        if clicking:
            print("Autoclicker running at 1.5 sec delay, press k to disable")
        else:
            print("Autoclicker disabled")


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
