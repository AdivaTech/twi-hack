"""
========================================================
Twi-Hack RP2350 – AES Encryption + SD Card Storage Demo
========================================================

This example demonstrates:
- AES-128 encryption using CircuitPython's aesio module
- Secure storage of encrypted data on an SD card
- Reading and decrypting the data back
- Intended for RP2350-based Twi-Hack hardware
- Educational / demonstration purpose only

⚠️ Note:
- This is NOT a secure key management example.
- Keys/IVs are hardcoded for learning purposes.
- Do NOT use this approach for real security products.
"""

import board
import busio
import sdcardio
import storage
import aesio


# ------------------------------------------------------
# Utility Functions: PKCS7 Padding
# ------------------------------------------------------
# AES works on fixed-size blocks (16 bytes).
# PKCS7 padding ensures plaintext fits perfectly.

def pad(data: bytes, block_size: int = 16) -> bytes:
    """
    Pad data to a multiple of block_size using PKCS7.
    """
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len


def unpad(data: bytes) -> bytes:
    """
    Remove PKCS7 padding after decryption.
    """
    pad_len = data[-1]
    return data[:-pad_len]


# ------------------------------------------------------
# AES Configuration
# ------------------------------------------------------
# AES-128 requires:
# - 16-byte key
# - 16-byte IV (for CBC mode)

key = b"Sixteen byte key"     # 16 bytes = AES-128 key
iv  = b"Sixteen byte iv."     # 16 bytes Initialization Vector

# Example plaintext message
plaintext = b"hello my name is twi-hack"


# ------------------------------------------------------
# Encrypt the Data
# ------------------------------------------------------
# Pad plaintext to 16-byte boundary
padded = pad(plaintext)

# Allocate output buffer
encrypted = bytearray(len(padded))

# Create AES cipher object (CBC mode)
cipher = aesio.AES(key, aesio.MODE_CBC, IV=iv)

# Encrypt padded plaintext into buffer
cipher.encrypt_into(padded, encrypted)

print("🔒 Encrypted data:", encrypted)


# ------------------------------------------------------
# SD Card Setup & Mount
# ------------------------------------------------------
# SPI pin configuration for RP2350
spi = busio.SPI(
    clock=board.GP2,
    MOSI=board.GP3,
    MISO=board.GP4
)

# Chip Select pin
sdcard = sdcardio.SDCard(spi, board.GP5)

# Create FAT filesystem
vfs = storage.VfsFat(sdcard)

# Mount SD card at /sd
try:
    storage.mount(vfs, "/sd")
except OSError:
    # Already mounted
    pass


# ------------------------------------------------------
# Write Encrypted Data to SD Card
# ------------------------------------------------------
with open("/sd/encrypted.txt", "wb") as f:
    f.write(encrypted)

print("✅ Written encrypted data to /sd/encrypted.txt")


# ------------------------------------------------------
# Read Back and Decrypt Data
# ------------------------------------------------------
with open("/sd/encrypted.txt", "rb") as f:
    enc_data = f.read()

# Allocate buffer for decrypted padded data
decrypted_padded = bytearray(len(enc_data))

# Create new AES object for decryption
cipher = aesio.AES(key, aesio.MODE_CBC, IV=iv)

# Decrypt data
cipher.decrypt_into(enc_data, decrypted_padded)

# Remove padding
decrypted = unpad(decrypted_padded)

print("🔓 Decrypted text:", decrypted.decode("utf-8"))


"""
========================================================
Expected Output:
--------------------------------------------------------
🔒 Encrypted data: b'...binary data...'
✅ Written encrypted data to /sd/encrypted.txt
🔓 Decrypted text: hello my name is twi-hack
========================================================
"""

