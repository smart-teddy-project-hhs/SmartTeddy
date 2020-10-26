# Press Shift+F10 to execute it or replace it with your code.
import serial
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt

# return motion data separate from serial stream
def check_motion(data):
    temp = data
    substring = "motion:"
    if substring in temp:
        print(temp)
        return temp

# return light data separate from serial stream
def check_light(data):
    temp = data
    substring = "lumen:"
    if substring in temp:
        print(temp)
        return temp

# Set in communication port for your device. In this case it is for linux. For windows it is COM3 or COM4.
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
# Check which port is active
print(ser.name)

if __name__ == '__main__':
    while True:
        # Read serial and decode it from bytes to string
        try:
            arduinoData = ser.readline().decode()
            # print(arduinoData)
            tijd = time.asctime(time.localtime(time.time()))

            if arduinoData:
                with open("test_data.csv", "a") as f:
                    # localtime = time.asctime(localtime(time.time()))
                    motion = check_motion(arduinoData)
                    lumen = check_light(arduinoData)

                    opslag = [[tijd, motion, lumen]]
                    # maybe its better to store it in a list and add the list directly in this code line beneath
                    opslaginvoer = pd.DataFrame(opslag, columns=['Tijd', 'Motion', 'Lumen'])
                    opslaginvoer.to_csv('sensorData4.csv', sep='\t', header=None, encoding='utf-8', mode='a', index= False)
                    # old
                    # writer = csv.writer(f, delimiter=";")
                    # writer.writerow([tijd, motion, lumen])
                    # plt.show()
        except:
            print("An error has occured")
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# print("arduino lengte is " + "{" + arduinoData + "} " + str((len(arduinoData))))
