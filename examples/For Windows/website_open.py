# Browser control to open website
# WARNING: For demonstration and educational use only.

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel

# NeoPixel on GP25
pixels = neopixel.NeoPixel(board.GP25, 1, brightness=0.5, auto_write=True)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def blink(color, t=0.2):
    pixels[0] = color
    time.sleep(t)
    pixels[0] = (0,0,0)
    time.sleep(0.1)


# Blink yellow to indicate starting
blink((255, 255, 0), 0.5)

# Open Run dialog (Win+R)
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)

# Type YouTube URL and Enter
layout.write("https://www.kickstarter.com/projects/creative-labs/twihack")  # replace with your website
keyboard.send(Keycode.ENTER)

# Wait for page to load
time.sleep(5)

# Blink red while preparing to press Subscribe
blink((255, 0, 0), 0.5)


