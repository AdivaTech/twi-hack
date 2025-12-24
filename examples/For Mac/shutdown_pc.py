# TwiHack HID – macOS shutdown/restart via Apple menu
# DEMO ONLY

import time, random
import board, usb_hid, neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# -------- CONFIG --------
MODE = "shutdown"   # "shutdown" or "restart"
# ------------------------

pixel = neopixel.NeoPixel(board.GP25, 1, brightness=0.5, auto_write=True)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def set_color(c): pixel[0] = c
def blink(c, t=0.2):
    set_color(c); time.sleep(t)
    set_color((0,0,0)); time.sleep(0.1)

def press(*keys):
    keyboard.send(*keys)
    time.sleep(0.12 + random.uniform(0,0.08))

# --- Start ---
blink((255,255,0), 0.4)

# Open Apple menu (Ctrl + Fn + Power works on many Macs)
# More reliable: Cmd + Space → type "Shut Down"
press(Keycode.COMMAND, Keycode.SPACE)
time.sleep(0.6)

if MODE == "restart":
    layout.write("restart")
else:
    layout.write("shut down")

press(Keycode.ENTER)
time.sleep(0.8)

# Confirm dialog (Enter)
press(Keycode.ENTER)

set_color((255,0,0))  # red = action
