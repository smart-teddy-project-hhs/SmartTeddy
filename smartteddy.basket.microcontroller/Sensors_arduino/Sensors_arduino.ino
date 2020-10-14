#define PIR_MOTION_SENSOR 2//Use pin 2 to receive the signal from the module
#define LIGHT_SENSOR A5 // Use analog A5 to read data from light sensor

//String lumen;
//String motion;

unsigned long previousTime = 0;
const long timeInterval = 5000; // ten seconds

void setup()
{
  pinMode(PIR_MOTION_SENSOR, INPUT); // set pins on input
  Serial.begin(9600);  // set baudrate to 9600 for serial monitor
}

void loop()
{
  unsigned long currentTimems = millis();
  if (currentTimems - previousTime >= timeInterval) {
    previousTime = currentTimems;
    if (digitalRead(PIR_MOTION_SENSOR)) //detects motion
      Serial.println("motion:True");
    else
      Serial.println("motion:False");
    if (analogRead(LIGHT_SENSOR)) {
      int light = analogRead(LIGHT_SENSOR);
      String L = String(light);
      Serial.println("lumen:" + L);
    }
  }
}
