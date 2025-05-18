from microbit import *
import random
while True:
    if accelerometer.was_gesture("shake"):
        choice = random.choice(["Rock", "Paper", "Scissors"])
        display.scroll(choice)
