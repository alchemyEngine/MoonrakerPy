# MoonrakerPy

**WIP!**

A Python convenience package for simplified interfacing with the [Moonraker](https://github.com/Arksine/moonraker) API. Essentially a `requests` wrapper.

## Installation
From PyPI:

    pip install moonrakerpy

## Basic Usage

```py
import moonrakerpy as moonpy

# Instantiate a `MoonrakerPrinter` object using the web/IP address of the target
# Moonraker installation.
printer = moonpy.MoonrakerPrinter('http://192.168.1.69')

# Send arbitrary g-code commands
printer.send_gcode('G28 X')

# Set temperatures
printer.set_extruder_temp(245)
printer.set_bed_temp(105)

# Read in g-code terminal messages
for msg in printer.get_gcode(count=5):
    printer(msg)
```
