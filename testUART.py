import serial
import time

def main():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

    try:
        for i in range(256):
            ser.write(bytes([i]))
            time.sleep(0.01) 

            response = ser.read()
            if response:
                print(f'Sent: {i}, Received: {ord(response)}')
            else:
                print(f'Sent: {i}, No response')

    finally:
        ser.close()

if __name__ == '__main__':
    main()