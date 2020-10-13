# Arduino Uno 
The data from the sensors is collected by a microcontroller. In this case an Arduino Uno. The arduino uses a grove shield to connect the grove sensors. 

## Installation

Check if all the sensors are attached on the correct pins of the grove shield. Connect the arduino uno to the computer with an USB-a to USB-b cable.

## Launching methods

The arduino will automatically start and read data from its attached sensors. The data is sending over serial.

## Hardware and software libraries

### Basket

The hardware for the basket contains an *Arduino Uno* microcontroller reads sensors and the *Asus Mini PC PN-50* runs an Python application for sending sending messages and communicates data inside the SwD home.

Sensors for the microcontroller light, gas, motion, speech, and camera.

* Light Dependent Resistor (LDR) - Light sensor
* Carbon Monoxide, Coal Gas, Liquified Gas meter (MQ9) - Gas sensor
* Grove - Speech Recognizer
* PIR - Motion sensor

Software of the following technologies are used.

Arduino IDE


