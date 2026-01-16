
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

guess = 0

while True:
    keyboard.type(f"{guess:04d}")  
    time.sleep(0.2)  
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    guess += 1

    if guess > 9999:
        guess = 0  

    time.sleep(1)  


