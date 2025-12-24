# CircuitPython HID script to open multiple Command Prompts rapidly (may hang PC)
# WARNING: For demonstration and educational use only.

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel
import random

# --- CONFIG ---
NUM_WINDOWS = 20          # Number of windows to open (adjust for severity)
DELAY_BETWEEN = 0.15      # Seconds between opening each window

pixels = neopixel.NeoPixel(board.GP25, 1, brightness=0.7, auto_write=True)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def blink(rgb, t=0.15):
    pixels[0] = rgb
    time.sleep(t)
    pixels[0] = (0, 0, 0)
    time.sleep(0.07)

def press_hotkey(*keys):
    keyboard.send(*keys)
    time.sleep(0.08 + random.uniform(0, 0.04))

def type_text(text):
    layout.write(text)
    time.sleep(0.09 + random.uniform(0, 0.04))

def press_enter():
    keyboard.send(Keycode.ENTER)
    time.sleep(0.08 + random.uniform(0, 0.03))

# Start sequence
blink((255, 255, 0), 0.4)  # Yellow blink to warn

for i in range(NUM_WINDOWS):
    blink((0, 255, 0), 0.12)  # Green blink per window
    # Open Run dialog (Win+R)
    press_hotkey(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.05)
    type_text("cmd")
    time.sleep(0.05)
    press_enter()
    time.sleep(DELAY_BETWEEN)

# Final red blink to indicate done
blink((255, 0, 0), 0.8)
pixels[0] = (0, 0, 0)
