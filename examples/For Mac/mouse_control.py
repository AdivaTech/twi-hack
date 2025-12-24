### TwiHack HID – Mouse Control Demo (Linux / macOS / Windows/ Android)
#⚠️ This demo is for educational and UI-automation purposes only.
'''
This demo uses USB HID mouse emulation and works across all major OSes.

#### macOS Users
You must allow the device:
- System Settings → Privacy & Security
  - Enable **Input Monitoring**
  - Enable **Accessibility**

#### Linux Users
No special permissions required.
'''

import time
import board
import usb_hid
import neopixel
import random
from adafruit_hid.mouse import Mouse

# ---------------- CONFIG ----------------
PIXEL_PIN = board.GP25
PIXEL_BRIGHTNESS = 0.4
MOVE_DELAY = 0.03
RANDOM_MOVES = 6
# --------------------------------------

pixel = neopixel.NeoPixel(PIXEL_PIN, 1, brightness=PIXEL_BRIGHTNESS, auto_write=True)
mouse = Mouse(usb_hid.devices)

def blink(color, t=0.25):
    pixel[0] = color
    time.sleep(t)
    pixel[0] = (0, 0, 0)
    time.sleep(0.1)

def smooth_move(dx, dy, steps=40):
    step_x = int(dx / steps)
    step_y = int(dy / steps)
    for _ in range(steps):
        mouse.move(step_x, step_y)
        time.sleep(MOVE_DELAY)

def square_pattern(size=300):
    smooth_move(size, 0)
    smooth_move(0, size)
    smooth_move(-size, 0)
    smooth_move(0, -size)

# -------- START --------
blink((255, 255, 0), 0.5)  # Yellow = start

# Random jitter demo
pixel[0] = (0, 0, 255)     # Blue = random movement
for _ in range(RANDOM_MOVES):
    mouse.move(
        random.randint(-120, 120),
        random.randint(-120, 120)
    )
    time.sleep(0.4)

# Click demo
pixel[0] = (255, 0, 0)     # Red = clicking
mouse.click(Mouse.RIGHT_BUTTON)
time.sleep(0.5)
mouse.click(Mouse.LEFT_BUTTON)

# Pattern movement
pixel[0] = (0, 255, 0)     # Green = pattern
square_pattern()

blink((0, 255, 255), 0.6)  # Cyan = done
pixel[0] = (0, 0, 0)
