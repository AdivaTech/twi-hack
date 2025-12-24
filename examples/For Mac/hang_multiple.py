# TwiHack HID – macOS Terminal Demo (SAFE)
# Educational / Demo use only

import time
import board
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# -------- CONFIG (SAFE DEFAULTS) --------
NUM_TERMINALS = 20
DELAY_BETWEEN = 0.05
# --------------------------------------

pixel = neopixel.NeoPixel(board.GP25, 1, brightness=0.5, auto_write=True)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def blink(color, t=0.25):
    pixel[0] = color
    time.sleep(t)
    pixel[0] = (0, 0, 0)
    time.sleep(0.1)

# Start
blink((255, 255, 0), 0.5)

for i in range(NUM_TERMINALS):
    blink((0, 0, 255), 0.2)
    keyboard.send(Keycode.COMMAND, Keycode.SPACE)
    time.sleep(0.8)
    layout.write("Terminal")
    keyboard.send(Keycode.ENTER)
    time.sleep(DELAY_BETWEEN)

blink((255, 0, 0), 0.6)
pixel[0] = (0, 0, 0)
