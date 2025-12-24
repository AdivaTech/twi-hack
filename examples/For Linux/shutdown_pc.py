# TwiHack HID – Linux shutdown/restart (sudo-aware)
# DEMO ONLY – do not hardcode real passwords

import time, random
import board, usb_hid, neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# -------- CONFIG --------
MODE = "shutdown"          # "shutdown" or "restart"
DELAY_SECONDS = 0          # 0 = immediate
SUDO_PASSWORD = "123456"   # DEMO ONLY
TERMINAL_DELAY = 2
SUDO_PROMPT_DELAY = 2
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

def type_cmd(cmd):
    layout.write(cmd)
    press(Keycode.ENTER)

# --- Start ---
blink((255,255,0), 0.4)          # yellow start

# Open Terminal (Ctrl+Alt+T)
press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
time.sleep(TERMINAL_DELAY)

set_color((0,0,255))              # blue typing

if MODE == "restart":
    cmd = f"sudo shutdown -r now"
else:
    cmd = f"sudo shutdown -h now"

type_cmd(cmd)

# Wait for sudo prompt, then type password
time.sleep(SUDO_PROMPT_DELAY)
layout.write(SUDO_PASSWORD)
press(Keycode.ENTER)

set_color((255,0,0))              # red = action
