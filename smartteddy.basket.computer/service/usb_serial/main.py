# Press Shift+F10 to execute it or replace it with your code.
from serial import Serial
import csv
import time

def main():
    print('in USB')
    # Set in communication port for your device. In this case it is for linux. For windows it is COM3 or COM4.
    ser = Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
    # Check which port is active
    print(ser.name)

    if __name__ == 'usb_serial.main':
        with open("/home/vftp/admin/arduino_data.csv", 'w') as csvfile:
            fieldnames = ["light sensor", "motion sensor", "sound sensor", "piezo sensor", "gas sensor value", "gas sensor ratio", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        while True:
            # Read serial and decode it from bytes to string
            try:
                # Receives sensor data in this order : light sensor data , motion sensor data , sound sensor data ,
                # piezo sensor data , gas sensor value and gas sensor ratio.
                arduinoData = ser.readline().decode()
                # print(arduinoData)
                date = time.asctime(time.localtime(time.time()))

                if arduinoData:
                    print(arduinoData)
                    with open("/home/vftp/admin/arduino_data.csv", "a") as f:
                        writer = csv.writer(f, delimiter=';')
                        split = arduinoData.split(";")
                        split.append(date)
                        writer.writerow(split)

            except:
                print("An error has occured or program is stopped")
                break
