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

* [Vosk API](https://alphacephei.com/vosk/) - A lightweight successor on the open source [CMU-Sphinx](https://cmusphinx.github.io/) speech recognition project 

* [Kaldi NL](https://github.com/opensource-spraakherkenning-nl/Kaldi_NL) - Open source medium weight (1,7 GB) speech recognition model from [Stichting Open Spraaktechnologie](https://openspraaktechnologie.org/download/) by teachers from the Universiteit Twente, Dutch Instituut voor Beeld en Geluid, and Radboud Universiteit Nijmegen. The download for the Vosk model can be found at [Kaldi Dutch model Vosk](https://alphacephei.com/vosk/models/vosk-model-nl-spraakherkenning-0.6.zip) from [Vosk models](https://alphacephei.com/vosk/models)

* [VU-sentiment-lexicon](https://github.com/opener-project/VU-sentiment-lexicon) - [Dutch Lexicon](https://github.com/opener-project/VU-sentiment-lexicon/tree/master/VUSentimentLexicon/NL-lexicon) with values of sentiment combined with a word, which is a project from the Vrije Universtieit Amsterdam from the year 2016.

* [Django-pytest](https://pytest-django.readthedocs.io/) - A test framework based on [Pytest](https://docs.pytest.org/) a Python test framework supports easiness. Besides it has a plugin for our favorite IDE Pycharm.

## Contributing 

Please read [CONTIBUTING.md](https://github.com/hwpvanholsteijn/Smartteddy/blob/master/CONTRIBUTING.md) in the root of the repository and contribute by adding your own services.

For additional support look in the wiki's on github and additional architectural documentation can asked from the contibutors in the section contact. 

### Code of Conduct

When contributing to the Smart Teddy project the rules for the [CODE_OF_CONDUCT.md](https://github.com/hwpvanholsteijn/Smartteddy/blob/master/CODE_OF_CONDUCT.md) apply. These are social rules in order to manage the contribution of the project.

## Contact 

Please feel free to send an e-mail in case of the Smart Teddy project, when documentation is insufficient.

[Huub van Holsteijn](mailto:h.w.p.vanholsteijn@student.hhs.nl]) - hwpvanholsteijn

[Szymon Jasinski](mailto:s.jasinski@student.hhs.nl) - polskaszym

[Jeoffrey Oostrom](mailto:j.s.oostrom@student.hhs.nl) - Jeoffrey-Oostrom

## License

Smart Teddy uses the [MIT License](https://mit-license.org/) which means that authors or copyright holders in no event shall be liable for any claim, damages or other liability, whether in an action of contract.

**Besides this we like to ask you to fork the project in case of reuse, so that we can see future progress on our project.** 😉
 
