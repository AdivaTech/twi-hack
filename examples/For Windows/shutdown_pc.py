# Demo Script to shutdown or restart a Windows PC via Run dialog.
# SAFETY: Use only on machines you own or have permission to control.
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
# Set how many seconds until shutdown/restart (Windows 'shutdown /s /t N' or /r).
# Use 0 for immediate action, or e.g. 30 for a 30s countdown.
SHUTDOWN_DELAY_SECONDS = 2

# Choose mode: "shutdown" or "restart"
MODE = "shutdown"   # or "restart"

# --- Hardware / HID setup ---
pixels = neopixel.NeoPixel(board.GP25, 1, brightness=0.5, auto_write=True)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# --- Visual helpers ---
def set_color(rgb):
    pixels[0] = rgb

def blink(rgb, times=2, on=0.12, off=0.08):
    for _ in range(times):
        pixels[0] = rgb
        time.sleep(on)
        pixels[0] = (0,0,0)
        time.sleep(off)

# --- Typing helpers ---
def human_delay(base=0.03, jitter=0.02):
    time.sleep(base + random.uniform(0, jitter))

def type_text(text, char_delay=0.02):
    layout.write(text)
    time.sleep(char_delay + random.uniform(0, 0.02))

def press_enter():
    keyboard.send(Keycode.ENTER)
    time.sleep(0.08 + random.uniform(0, 0.06))

def press_hotkey(*keys):
    keyboard.send(*keys)
    time.sleep(0.12 + random.uniform(0, 0.08))

# --- Shutdown/Restart sequence (Windows) ---
def windows_shutdown(delay_seconds=30, restart=False):
    # Visual: short amber blink to warn
    blink((255, 160, 0), times=3, on=0.14, off=0.06)
    set_color((255, 60, 60))  # red-ish while preparing
    # Open Run dialog
    press_hotkey(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.35)
    # Build the shutdown/restart command
    if restart:
        cmd = "shutdown /r /t {}".format(int(delay_seconds))
    else:
        cmd = "shutdown /s /t {}".format(int(delay_seconds))
    # Type the command
    type_text(cmd)
    press_enter()
    # Provide a blinking countdown visual for the configured time
    if delay_seconds > 0:
        # blink faster as countdown approaches 0
        for remaining in range(delay_seconds, 0, -1):
            if remaining > 5:
                blink((255, 0, 0), times=1, on=0.06, off=0.94)
            else:
                blink((255, 0, 0), times=1, on=0.12, off=0.88)
        # final confirmation blink
        for _ in range(4):
            set_color((255,0,0))
            time.sleep(0.08)
            set_color((0,0,0))
            time.sleep(0.06)
    else:
        # immediate
        for _ in range(6):
            set_color((255,0,0))
            time.sleep(0.05)
            set_color((0,0,0))
            time.sleep(0.05)

# --- Main ---
# caution message (LED)
set_color((0, 200, 50))  # green ready
time.sleep(0.25)
set_color((0,0,0))
time.sleep(0.15)

# Run the Windows shutdown or restart (set MODE to "shutdown" or "restart")
windows_shutdown(delay_seconds=SHUTDOWN_DELAY_SECONDS, restart=(MODE=="restart"))

# turn off LED (device done)
set_color((0,0,0))