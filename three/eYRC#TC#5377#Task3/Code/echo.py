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
PORT = "COM5"
# MAC_PORT: Port for MacOS.
MAC_PORT = r"/dev/tty.SLAB_USBtoUART"


if __name__ == "__main__":
    with serial.Serial(MAC_PORT, 9600, timeout=0.005) as ser:
        # Flush buffers.
        ser.flushInput()
        ser.flushOutput()
        
        while True:
            user_input = input("Enter key: ")
            # Send bytes data.
            ser.write(user_input.encode())
            # Wait for microcontroller to start buffering.
            time.sleep(0.1)
            # Read from microcontroller.
            line = ser.readline()
            # Print all data without a new line. New line should be send from microcontroller.
            print(line.decode(), end='')
