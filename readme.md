# Twi‑Hack — Compact, Triple‑Port HID Injection Dongle

Twi-Hack is a compact ethical-hacking & prototyping dongle with USB-A, USB-C and USB-A (female) ports and a powerful Raspberry Pi RP2350A MCU — the most versatile pocket HID toolbox for learners, pentesters, and makers.

### Features:
- Powered by RP2350 which is Dual-core Arm Cortex-M33 (ARMv8-M) or Hazard3 RISC-V (RV32IMAC+) cores, running at up to 150 MHz 
- Dual USB (Type-A & Type-C) – Direct plug-and-play to PC for Ethical hacking & testing
- Memory - 520KB of SRAM, and 8 MB of onboard Flash memory
- Additional Female Type A USB Host - to connect HID like keyboard, mouse. It allows remapping any key your way. 
- SD Card Support – Store payloads, scripts, and data easily
- Compact Size – Pocket-friendly design, carry your hacking lab anywhere
- Programming Language - C/C++, Arduino, MicroPython/CircuitPython

### Hardware Pinout:
<img src="https://github.com/AdivaTech/twi-hack/blob/main/images/twi-hack_pinout.PNG" weight="440" height="251">

### Software Setup and Installation:
* Download and Install Thonny IDE from [here](https://thonny.org/)

  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/thonny_ide.PNG" weight="560" height="336">
  
* Press Hold BOOT button and connect to laptop/PC, now Twi-Hack device is in boot mode you will see RP2350 device folder open as shown below:

  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/rp2350_device.PNG" weight="530" height="340">
  
* By default you will receive device with Circuitpython pre-installed, but no worry you can re-install as shown here if interested otherwise direct jump to next step for code testing.
* So, to install just open thonny IDE with Twi-hack device connected. At bottom corner when clicked you will see install option both MicroPython & CircuitPython because device is in boot mode. To use HID features you are required to select CircuitPython option.

  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/circuitpython_install.png" weight="816" height="436">
  
* Select properly Target, family and variant as shown below and click install once done close.

  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/target_selection.png" weight="329" height="312">
  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/target_install.PNG" weight="329" height="312">
  
* Once installation successfull automatically device will be listed as circuitpy as shown with folder having few default files and folder.

  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/circuitpython_device.png" weight="820" height="435">
  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/circuitpython_device_folder.png" weight="637" height="343">

### Example Code Testing:
* Once everything setup download this github which contains example codes and lib files

  <img src="https://github.com/AdivaTech/twi-hack/blob/main/images/circuitpython_device_folder.png" weight="637" height="343">
