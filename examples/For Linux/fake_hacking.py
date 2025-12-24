# TwiHack HID – Linux Fake Hacking (sudo-aware)
# DEMO ONLY – do not hardcode real passwords

import time
import board
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# ---------------- CONFIG ----------------
SUDO_PASSWORD = "123456"   # <-- DEMO ONLY, your password
TERMINAL_DELAY = 2
SUDO_PROMPT_DELAY = 2
# ---------------------------------------

pixel = neopixel.NeoPixel(board.GP25, 1, brightness=0.4, auto_write=True)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def blink(color, t=0.3):
    pixel[0] = color
    time.sleep(t)
    pixel[0] = (0, 0, 0)
    time.sleep(0.1)

def enter():
    keyboard.send(Keycode.ENTER)
    time.sleep(0.3)

def sudo_password():
    time.sleep(SUDO_PROMPT_DELAY)
    layout.write(SUDO_PASSWORD)
    enter()

# -------- START --------
blink((255, 255, 0))  # Yellow = start

# Open Terminal (Ctrl + Alt + T)
keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
time.sleep(TERMINAL_DELAY)

pixel[0] = (0, 0, 255)  # Blue = typing

# sudo apt install cmatrix
layout.write("sudo apt install -y cmatrix")
enter()
sudo_password()

time.sleep(6)

blink((255, 0, 0))  # Red = demo running

# Run cmatrix
layout.write("cmatrix -b")
enter()

pixel[0] = (0, 255, 0)  # Green = active
