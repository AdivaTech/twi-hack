# Twi-Hack RP2350 – Ubuntu Camera Demo (Cheese)
# Educational HID automation example

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel

# NeoPixel status LED
pixels = neopixel.NeoPixel(board.GP25, 1, brightness=0.4, auto_write=True)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def blink(color, t=0.25):
    pixels[0] = color
    time.sleep(t)
    pixels[0] = (0, 0, 0)
    time.sleep(0.1)

# --- Start ---
blink((255, 255, 0), 0.5)  # Yellow = start

# Open application launcher (Super key)
keyboard.send(Keycode.WINDOWS)
time.sleep(0.6)

# Launch Cheese camera
layout.write("cheese")
time.sleep(0.3)
keyboard.send(Keycode.ENTER)

blink((0, 255, 0), 0.4)  # Green = app launched
time.sleep(3)           # Wait for camera app

# Start recording (Space)
pixels[0] = (255, 0, 0)
keyboard.send(Keycode.SPACE)
time.sleep(5)

# Stop recording
keyboard.send(Keycode.SPACE)
pixels[0] = (0, 0, 0)

blink((0, 255, 255), 0.4)  # Cyan = done
