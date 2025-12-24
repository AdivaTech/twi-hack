# TwiHack HID – Linux Terminal Demo (SAFE)
# Educational / Demo use only

import time
import board
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# -------- CONFIG (SAFE DEFAULTS) --------
NUM_TERMINALS = 20      # Increase cautiously
DELAY_BETWEEN = 0.01   # Slower = safer
# --------------------------------------

pixel = neopixel.NeoPixel(board.GP25, 1, brightness=0.5, auto_write=True)
keyboard = Keyboard(usb_hid.devices)

def blink(color, t=0.25):
    pixel[0] = color
    time.sleep(t)
    pixel[0] = (0, 0, 0)
    time.sleep(0.1)

# Start
blink((255, 255, 0), 0.5)  # Yellow = start

for i in range(NUM_TERMINALS):
    blink((0, 255, 0), 0.2)
    keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
    time.sleep(DELAY_BETWEEN)

blink((255, 0, 0), 0.6)  # Red = done
pixel[0] = (0, 0, 0)
