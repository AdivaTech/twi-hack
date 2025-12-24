"""
Twi-Hack RP2350 – SD Card Read/Write Demo
---------------------------------------
- Initialize SD card over SPI
- Create multiple text files
- Read files back from SD card
"""

import board
import busio
import sdcardio
import storage

# SPI pins (GP2=SCK, GP3=MOSI, GP4=MISO)
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

# SD card chip-select on GP5
sdcard = sdcardio.SDCard(spi, board.GP5)

# Mount SD card at /sd
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
print("SD card mounted")

# Create 5 text files
for i in range(1, 6):
    filename = f"/sd/file{i}.txt"
    with open(filename, "w") as f:
        f.write("Hello World\n")
    print(f"Created {filename}")

# Read files back
print("\nReading files:")
for i in range(1, 6):
    filename = f"/sd/file{i}.txt"
    with open(filename, "r") as f:
        print(f"{filename}: {f.read().strip()}")
