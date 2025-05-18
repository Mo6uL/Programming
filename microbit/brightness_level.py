from microbit import *

while True:
    brightness = display.read_light_level() // 25  # scale 0-9
    display.show(str(brightness))
