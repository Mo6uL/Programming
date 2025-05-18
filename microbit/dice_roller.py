from microbit import *
import random
while True:
    if button_a.was_pressed():
        roll = random.randint(1, 6)
        display.show(str(roll))
