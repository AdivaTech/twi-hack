# Camera control takes over
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

# Open Windows Search (Win+S)
keyboard.send(Keycode.WINDOWS, Keycode.S)
time.sleep(0.5)

# Blink green to indicate Camera is launching
pixels[0] = (0, 255, 0)

# Type "Camera"
layout.write("Camera")
time.sleep(0.2)
pixels[0] = (0, 0, 255) # Blink blue to indicate ready

# Press Enter to open Camera app
keyboard.send(Keycode.ENTER)
time.sleep(2) # Wait for app to open

# Start recording
pixels[0] = (255, 0, 0)  # Blink RED to indicate recording
keyboard.send(Keycode.CONTROL, Keycode.ENTER)
time.sleep(5)

# Press Enter to open Camera app
keyboard.send(Keycode.CONTROL, Keycode.SPACE)
pixels[0] = (0, 0, 0)  # Blink RED to indicate recording

# Wait for app to open
time.sleep(2)