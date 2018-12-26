import serial
import time

PORT = "COM5"
MAC_PORT = r"/dev/tty.SLAB_USBtoUART"

if __name__ == "__main__":
    with serial.Serial(MAC_PORT, 9600, timeout=0.005) as ser:
        ser.flushInput()
        ser.flushOutput()
        while True:
            user_input = input("Enter key: ")
            ser.write(user_input.encode())
            time.sleep(0.1)
            line = ser.readline()
            print(line)
