# Smart Teddy

With the intention of the Smart Teddy we want to take away worries of caregivers for Seniors with Dementia (SwD). Examples of caregivers are family memembers or medical staff that provide care to the SwD. Because by monitoring the safety of a SwD, they can live home longer without residating in a care home. In order to monitor the person of age we provided a Smart Teddybear and basket.

For motoring the SwD microcontrollers were first choice of implementation, because the provide easy access to low-level motoring sensors. The Smart Teddy and basket both have a microcontoller to have two monitoring points for extra validity. The basket reads the microcontroller basket via a Personal Computer (PC)

Additional information technologies, launching methods, the Smart Teddy project can be found in the README.

## Hardware and software libraries

### Basket

The hardware for the basket contains an Arduino Uno microcontroller reads sensors and the Asus PN-50 mini pc runs an Python application for sending sending messages and communicates data inside the SwD home.

Sensors for the microcontroller light, gas, motion, speech, and camera.

* Light Dependent Resisto r(LDR) - Light sensor
* Carbon Monoxide, Coal Gas, Liqiefied Gas meter (MQ9) - Gas sensor
* Grove - Speech Recognizer
* PIR - Motion sensor

Software of the following technologies are used.

* Bleak - Bluetooth library for Generic Attribute Profile (GATT) communication
