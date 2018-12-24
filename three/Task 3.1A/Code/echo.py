import serial
import time

PORT = "COM5"
MAC_PORT = r"/dev/tty.SLAB_USBtoUART"

if __name__ == "__main__":
    ser = serial.Serial("/dev/tty.SLAB_USBtoUART", 9600, timeout=0.005)
    while True:
        user_input = input("Enter key: ")
        ########## ENTER YOUR CODE HERE ############

        ser.write(user_input.encode())

        res = ser.readline()
        print(res)

        ############################################
