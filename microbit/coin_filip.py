from microbit import *
import random
while True:
    if button_a.was_pressed():
        coin = random.choice(["Heads", "Tails"])
        display.scroll(coin)
