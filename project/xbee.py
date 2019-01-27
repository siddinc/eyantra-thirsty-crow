'''
* Team Id : 5377
* Author List : Vikrant Gajria
* Filename: echo.py
* Theme: TC -- Specific to eYRC
* Functions: None (only __main__ block)
* Global Variables: PORT, MAC_PORT
'''
import serial
import time

# PORT: Port for Windows machines.
PORT = r"COM5"
# MAC_PORT: Port for MacOS.
MAC_PORT = r"/dev/tty.SLAB_USBtoUART"


def send(command):
    with serial.Serial(MAC_PORT, 9600, timeout=0.005) as ser:
        # Flush buffers.
        ser.flushInput()
        ser.flushOutput()
        
        # Send bytes data.
        ser.write(command.encode())
        # Wait for microcontroller to start buffering.
        time.sleep(0.1)
