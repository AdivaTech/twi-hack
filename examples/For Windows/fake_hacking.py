# WARNING: For demonstration and educational use only.

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel

# --- Configuration and Initialization ---
# NeoPixel on GP25 (adjust if your board uses a different pin)
pixels = neopixel.NeoPixel(board.GP25, 1, brightness=0.5, auto_write=True)

# Initialize HID components
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# --- Helper Functions ---
def set_pixel_color(color):
    """Sets the NeoPixel color immediately."""
    pixels[0] = color

def blink(color, t=0.2):
    """Blinks the NeoPixel once."""
    set_pixel_color(color)
    time.sleep(t)
    set_pixel_color((0, 0, 0)) # Turn off
    time.sleep(0.1)

def type_command(cmd, delay=0.05):
    """Types a string and presses Enter."""
    layout.write(cmd)
    time.sleep(delay)
    keyboard.send(Keycode.ENTER)
    time.sleep(0.1) # Short wait after pressing Enter

# --- Main Script Sequence ---

# 1. Blink yellow to indicate the script is starting
blink((255, 255, 0), 0.5)

# 2. Open the Run dialog (Win + R)
set_pixel_color((0, 0, 255)) # Solid blue for command execution
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)

# 3. Type "cmd" and press Enter to open Command Prompt
layout.write("cmd")
time.sleep(0.2)
keyboard.send(Keycode.ENTER)
time.sleep(0.2)
keyboard.send(Keycode.F11)

# Wait for the Command Prompt window to open and stabilize
time.sleep(1.5)

# 4. Start the 'Hacking' sequence
set_pixel_color((0, 255, 0)) # Green for system access

# Set terminal colors to classic 'hacker' green on black
type_command("color 0a")

# Change the window title
type_command("title ACCESS GRANTED: [Initializing] > Mainframe_01")

# Display a dramatic message
type_command("echo [STATUS: ONLINE] Beginning Data Enumeration...")
time.sleep(1)

# Run 'tree' to quickly fill the screen with "busy work"
blink((255, 165, 0), 0.1) # Orange blink
type_command("tree")
time.sleep(1) # Let the tree command start running

# Final command: Endless ping loop (looks like constant network activity)
set_pixel_color((255, 0, 0)) # Solid Red for "Active Hacking"
type_command("echo Starting Persistent Network Trace (Press Ctrl+C to stop the trace)")
time.sleep(0.5)
type_command("ping -t 8.8.8.8", delay=0.0) # Ping Google DNS infinitely (until Ctrl+C)

# Sequence finished, pixel remains red until unplugged or reset
print("Hacking sequence complete!")