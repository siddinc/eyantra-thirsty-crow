"""
* Team Id : 5377
* Author List : Vikrant Gajria
* Filename: echo.py
* Theme: TC -- Specific to eYRC
* Functions: None (only __main__ block)
* Global Variables: PORT, MAC_PORT
"""
import serial
import time

# PORT: Port for Windows machines.
PORT = r"COM5"
# MAC_PORT: Port for MacOS.
# MAC_PORT = r"/dev/tty.SLAB_USBtoUART"
MAC_PORT = r"/dev/ttys001"

SER = serial.Serial(MAC_PORT, 9600, timeout=0.005)

def send_xbee(command):
    # Flush buffers.
    SER.flushInput()
    SER.flushOutput()

    # Send bytes data.
    SER.write(command.encode())
    # Wait for microcontroller to start buffering.
    time.sleep(0.1)

def read_xbee_forever():
    while True:
        l = SER.read()
        if l:
            print(l.decode())
            break

if __name__ == "__main__":
	from threading import Thread
	t = Thread(target=read_xbee_forever)
	t.start()
	while 1:
		x = input(">> ")
