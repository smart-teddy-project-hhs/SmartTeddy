#include <SamdAudio.h>
SamdAudio AudioPlayer;

#include <SPI.h>
#include "SdFat.h"
#define error(msg) sd.errorHalt(F(msg))

#define NUM_AUDIO_CHANNELS 4 //could be 1,2 or 4 for sound

// SD chip select pin
#define YOUR_SD_CS 4

// SD chip select pin.  Be sure to disable any other SPI devices such as Enet.
const uint8_t chipSelect = 4;

const int SAMPLE_INTERVAL_MS = 2000;

// Log file base name.  Must be six characters or less.
#define FILE_BASE_NAME "Teddy"

SdFat sd;// File system object.

SdFile file; // Log file.

unsigned long logTime; // Time in micros for next data record.

//indicate sample rate here (use audacity to convert your wav)
const unsigned int sampleRate = 22050;
bool state = true;
uint32_t timer = 0, updatetimer = 0;

unsigned long startMillis = 0;  //some global variables available anywhere in the program
unsigned long currentMillis = 0;

unsigned long currentlogtime = 0;  //some global variables available anywhere in the program
unsigned long vorigelogtime = 0;

int logcounter = 0;
const unsigned long soundPeriod = 10000;  //the value is a number of milliseconds
const unsigned long logPeriod = 1000;  //the value is a number of milliseconds
const unsigned long dumpPeriod = 900000;  //the value is a number of milliseconds


const int bewegingSensorPin = 10;
const int sensorPin = A3;
const int smokeSensorPin = A5;

#define echoPin 11 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 12 //attach pin D3 Arduino to pin Trig of HC-SR04

long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

int sr04read = 0;
int pirRead = 0;
int micRead = 0;
int smokeRead = 0;

const uint8_t BASE_NAME_SIZE = sizeof(FILE_BASE_NAME) - 1;
char fileName[13] = FILE_BASE_NAME "00.csv";

bool musicPlaying = false;

int myMic[60];
int mySmoke[60];
int mySr04[60];
int myBark[60];
unsigned long timerun[60];

int dumpcounter = 0;


void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  pinMode(bewegingSensorPin, INPUT);
  Serial.begin(9600);
  Serial1.begin(9600);
  digitalWrite(13, HIGH);
  delay(2000);
  digitalWrite(13, LOW);
  Serial.println("Start Programma");
  Serial.print("Initializing SD card...");
  if (AudioPlayer.begin(sampleRate, NUM_AUDIO_CHANNELS, YOUR_SD_CS) == -1)
  {
    Serial.println(" failed!");
    return;
  }
  Serial.println(" done.");

  delay(1000);

  if (!sd.begin(chipSelect, SD_SCK_MHZ(50))) {
    sd.initErrorHalt();
  }

  // Find an unused file name.
  if (BASE_NAME_SIZE > 6) {
    error("FILE_BASE_NAME too long");
  }
  while (sd.exists(fileName)) {
    if (fileName[BASE_NAME_SIZE + 1] != '9') {
      fileName[BASE_NAME_SIZE + 1]++;
    } else if (fileName[BASE_NAME_SIZE] != '9') {
      fileName[BASE_NAME_SIZE + 1] = '0';
      fileName[BASE_NAME_SIZE]++;
    } else {
      error("Can't create file name");
    }
  }
  if (!file.open(fileName, O_WRONLY | O_CREAT | O_EXCL)) {
    //error("file.open");
    //file.clearError();
    Serial.print(F("opening problems"));
  }
  // Read any Serial data.
  // do {
  //   delay(10);
  //} while (Serial.available() && Serial.read() >= 0);

  Serial.print(F("Logging to: "));
  Serial.println(fileName);


  // Write data header.
  writeHeader();
  delay(1000);

  // Start on a multiple of the sample interval.
  logTime = millis() / (SAMPLE_INTERVAL_MS) + 1;
  logTime *= SAMPLE_INTERVAL_MS;


}


void loop()
{
  //pirRead = readPirSensor();
  micRead = readMicSensor();
  smokeRead = readSmokeSensor();
  sr04read = sr04();

  currentlogtime = millis();

  if (currentlogtime - vorigelogtime >= logPeriod && logcounter < 60)
  {
    timerun[logcounter] = (millis() / 1000 );
    myMic[logcounter] = micRead;
    mySmoke[logcounter] = smokeRead;
    mySr04[logcounter] = sr04read;
    myBark[logcounter] = musicPlaying;
    vorigelogtime = currentlogtime;
    logcounter++;
    dumpcounter++;
  }

  if (musicPlaying == false)
  {
    if (sr04read == HIGH || smokeRead == HIGH )
    {
      musicPlaying = true;
      AudioPlayer.play("bark.wav", 1);
      startMillis = millis();

      Serial.println("Playing file: bark.wav... ");
    }
  }
  else
  {
    if (micRead == HIGH)
    {
      AudioPlayer.stopChannel(1);
      musicPlaying = false;
      Serial.println("Channel 1 off!");
    }
    else
    {
      currentMillis = millis();
      if (currentMillis - startMillis >= soundPeriod)
      {
        musicPlaying = false;
        Serial.println("Finished playing file");
      }
      else
      {
        Serial.println("SOUND");
      }
    }
  }

  if (musicPlaying == false && logcounter >= 60)
  {
    for (int p = 0; p < 60; p++)
    {
      Serial.print(timerun[p]);
      Serial.print(',');
      Serial.print(myMic[p]);
      Serial.print(',');
      Serial.print(mySmoke[p]);
      Serial.print(',');
      Serial.print(mySr04[p]);
      Serial.print(',');
      Serial.println(myBark[p]);
      logData(p);
    }
    logcounter = 0;
  }

  if (musicPlaying == false && dumpcounter >= 45 && logcounter < 60)
  {
    dumpmyfile();
    Serial.println("FILE DUMPED");
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);

    dumpcounter = 0;
  }

}

int sr04()
{
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  delay(10);

  if (distance <= 10)
  {
    Serial.println("object gedetecteerd");
    return HIGH;
  }
  else return LOW;
}

int readSmokeSensor()
{
  int waarde = 0;
  int sensorValue = analogRead(smokeSensorPin);
  if (sensorValue >= 105 )
  {
    Serial.println("SMOKE DETECTED");
    waarde = HIGH;
    return waarde;
  }
  else
  {
    waarde = LOW;
    return waarde;
  }
}

int readMicSensor()
{
  int waarde = 0;
  int sensorValue = analogRead(sensorPin);
  if (sensorValue >= 600 || sensorValue <= 150 )
  {
    Serial.println("LOUDNESS DETECTED");
    waarde = HIGH;
    return waarde;
  }
  else
  {
    waarde = LOW;
    return waarde;
  }
}

int readPirSensor ()
{
  int pirSensor = digitalRead(bewegingSensorPin);

  if (pirSensor == HIGH )
  {
    Serial.println("Beweging gedetecteerd");
    return HIGH;
  }
  else
  {
    Serial.println(" ");
    return LOW;
  }
}

// Write data header.
void writeHeader() {
  file.print(F("Time"));

  file.print(F(",Barking"));
  file.print(F(",Smoke sensor"));
  file.print(F(",Mic"));
  file.print(F(",Movement sensor"));
  file.println();
}

// Log a data record.
void logData(int q) {
  if (q == 0 )
  {
    if (file.isOpen() == false)
    {
      if (!file.open(fileName, O_WRONLY | O_AT_END  ))
      {
        error("file cant open");
      }
    }
  }


  // Write data to file.  Start with log time in micros.
  file.print(timerun[q]);

  // Write ADC data to CSV record.
  file.write(',');
  file.print(myBark[q]);
  file.write(',');
  file.print(mySmoke[q]);
  file.write(',');
  file.print(myMic[q]);
  file.write(',');
  file.print(mySr04[q]);
  file.println();

  if (q >= 59 )
  {
    delay(500);
    // Force data to SD and update the directory entry to avoid data loss.
    if (!file.sync() || file.getWriteError()) {
      error("write error");
    }
    // Close file.
    file.close();
    Serial.println("wrote file and closed it");
    delay(200);
  }
}

void dumpmyfile()
{
  if (file.isOpen() == false)
  {
    if (file.open("Teddy00.csv")) {
      //Serial1.println("Teddy00.csv:");

      // read from the file until there's nothing else in it:
      while (file.available()) {
        //file.rewind();
        //Serial.write(file.read());
        //delay(500);
        Serial1.write(file.read());
        // Serial.println("DUMPED Teddy00.csv:");
      }
      // close the file:
      file.close();
      delay(500);
    } else {
      // if the file didn't open, print an error:
      Serial.println("error opening Teddy00.csv");
    }
  }
  else
  {
    Serial1.println("file is already open");
  }
}
