# Smart Teddy

The goal of the Smart Teddy is to make Seniors with Dementia (SwD) reside home longer by increasing their Quality of Life (QoL). In previous research, it is shown that residing Seniors have a higher QOL, compare to the seniors in a residential home. In that case, the Smart Teddy makes the senior with dementia live home longer by measuring its QoL.

The Smart Teddy project has a (Smart) Teddy and basket which performing measurements on the QoL. Examples of the QoL-measurements are basic health indicators and sentimental analysis. Which will give a basic answer to the question: 'How did you feel last week?' Normally, this question would be asked by informal-caregiver/formal-caregiver, therefore, automating this question will reduce strain on the caregivers. Generally, the Smart Teddy and basket will try to give a feeling of home sustaining the Quality of Life for senior and caregiver.

A summary of how to install the Smart Teddy project and guidance on how to launch the Smart Teddy Project can be found in the README. Additional information can be found in the Wiki on Github and the 'Developers manual' can be asked from the owners named in the chapter 'Contacts'.

**Technical Description**

Smart Teddy is a Internet-of-Things (IoT) project which is an other name for a collection network-enabled devices, excluding traditional computers like laptops and servers. The Smart Teddy does not communicate with cloud services to increase security. However, code-quality can be increased by cloud services. 

## Installation

The Smart Teddy Project consists of two devices with/without sub devices, below you can read the minimum requirements for these devices. First the Smart Teddy with a single microcontroller and second the basket with a computer and sub-microcontroller connected through USB.

1. Add a power cable to the basket computer
2. Turn on the basket computer
3. Set up a python virtual environment (pipenv) on the basket computer
4. Install the required programs for the basket computer through the Pipfile
   Note: some programs cannot be installed in the pipenv
5. Configure an user for the web-application
6. Connect the microcontroller to the computer through USB with the uploaded file via the IDE
7. Add the webcam to the computer via USB
8. Power the Smart teddy by a on/off switch
9. Pair the Smart Teddy with basket computer through wireless communication

## Launching methods

1. Turn on the basket computer
2. Make sure that the microcontrollers and webcam are connected properly
3. Login with the accepted credentials on the computer
4. change directory to smartteddy.bakset.computer and pipenv shell
5. `python3 web/smartteddydashboard/manage.py runserver` to run a development server
6. Open a new terminal to the smartteddy.bakset.computer directory and pipenv shell
7. `python3 service/start.py` to run all services
8. New terminal is required on smartteddy.bakset.computer this time without pipenv
9. `python3 service/speechrecognition/main.py` to run speech recognition

## Contributing 

Please read [CONTIBUTING.md](https://github.com/smart-teddy-project-hhs/SmartTeddy/blob/master/CONTRIBUTING.md) in the root of the repository and contribute by adding your own services.

For additional support, ask for 'Developers Manual' of the owners in the chapter Contacts for the additional architectural documentation. 

### Code of Conduct

When contributing to the Smart Teddy project the rules for the [CODE_OF_CONDUCT.md](https://github.com/smart-teddy-project-hhs/SmartTeddy/blob/master/CODE_OF_CONDUCT.md) apply. These are social rules in order to manage the contribution of the project.

## Contact 

Please feel free to send an e-mail in case of the Smart Teddy project, when documentation is insufficient or for extra guidance.

[Huub van Holsteijn](mailto:h.w.p.vanholsteijn@student.hhs.nl]) - hwpvanholsteijn

[Szymon Jasinski](mailto:s.jasinski@student.hhs.nl) - polskaszym

[Jeoffrey Oostrom](mailto:j.s.oostrom@student.hhs.nl) - Jeoffrey-Oostrom

## License

Smart Teddy uses the [MIT License](https://mit-license.org/) which means that authors or copyright holders in no event shall be liable for any claim, damages or other liability, whether in an action of contract. **However in MIT means that a NOTICE of the copyright owners is required.**

_Besides this we like to ask you to fork the project in case of reuse, so that we can see future progress on our project._ 
 
