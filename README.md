# Smart Teddy

With the intention of the Smart Teddy we want to take away worries of caregivers for Seniors with Dementia (SwD). Examples of caregivers are family members or medical staff that provide care to the SwD. Because by monitoring the safety of a SwD, they can live home longer without residing in a care home. In order to monitor the person of age we provided a Smart Teddy and basket.

For monitoring the SwD microcontrollers were first choice of implementation, because the provide easy access to low-level motoring sensors. The Smart Teddy and basket both have a microcontoller to have two monitoring points for extra validity. The basket reads the microcontroller basket via a Personal Computer (PC)

Additional information technologies and launching methods of the Smart Teddy project can be found in the README.

## Installation

Basket microcontoller - Check if all the sensors are attached on the correct pins of the grove shield. Connect the arduino uno to the computer with an USB-a to USB-b cable.
Basket computer - Open a terminal, git clone, pip install requirements.txt, then django is launchable.

## Launching methods

Basket microcontoller - start up the arduino IDE and upload the file to the arduino.
Basket computer - change directory to the basket folder and for development: `python manage.py runserver` or for production `python manage.py check --deploy`

## Hardware and software libraries

### Basket

The hardware for the basket contains an *Arduino Uno* microcontroller reads sensors and the *Asus Mini PC PN-50* runs an Python application for sending sending messages and communicates data inside the SwD home.

Sensors for the microcontroller light, gas, motion, speech, and camera.

* Light Dependent Resistor (LDR) - Light sensor
* Carbon Monoxide, Coal Gas, Liquified Gas meter (MQ9) - Gas sensor
* Grove - Speech Recognizer
* PIR - Motion sensor

Software libraries used for the basket microcontoller.

* millis - Setting time in milliseconds  

Software of the following technologies are used for the basket computer.

* [Django](https://www.djangoproject.com/) - Python web-framework for creating a Website or Application Programming Interface (API)

* [Bleak](https://github.com/hbldh/bleak) - Bluetooth library for Generic Attribute Profile (GATT) communication]

* [Wagtail-Flags](https://github.com/cfpb/wagtail-flags) - A feature toggling program for which is intergrated in the Django Admin Panel.
