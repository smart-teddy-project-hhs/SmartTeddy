#define PIR_MOTION_SENSOR 2//Use pin D2 to receive the signal from the module
#define GAS_SENSOR A0 // use analog port of the grove conenctor (A0) to read data from gas sensor
#define LIGHT_SENSOR A1 // Use analog port of the grove connector (A1) to read data from light sensor
#define SOUND_SENSOR A2 // use analog port of the grove conenctor (A2) to read data from sound sensor
#define PIEZO_SENSOR A3 //use analog port of the grove conenctor (A3) to read data from piezo sensor

bool motion;
byte lumen; 
int sound;
int piezo; 
float gas;

unsigned long previousTime = 0;
const long timeInterval = 10000; // ten seconds
float calibratedGas;

// initialise gas sensor
void initgas(){ 
    float sensor_volt;
    float RS_air; //  Get the value of RS via in a clear air
    float R0;  // Get the value of R0 via in H2
    float sensorValue;
  // Get a average data by testing 100 times
    for(int x = 0 ; x < 100 ; x++)
    {
        sensorValue = sensorValue + analogRead(GAS_SENSOR);
    }
    sensorValue = sensorValue/100.0;
    sensor_volt = sensorValue/1024*5.0;
    RS_air = (5.0-sensor_volt)/sensor_volt; // omit * RL
    calibratedGas = RS_air/9.8; // The ratio of RS/R0 is 9.8 in a clear air from Graph (Found using WebPlotDigitizer)
}

void setup()
{
  pinMode(PIR_MOTION_SENSOR, INPUT); // set pins on input
  Serial.begin(9600);  // set baudrate to 9600 for serial monitor
  initgas();
}

void loop()
{
  motion = false;
  lumen= 0;
  float sensorV;
  float ratio;
  
  unsigned long currentTimems = millis();
  if (currentTimems - previousTime >= timeInterval) {
    previousTime = currentTimems;
    motion = digitalRead(PIR_MOTION_SENSOR);
    lumen = analogRead(LIGHT_SENSOR);
    sound = analogRead(SOUND_SENSOR);    
    piezo = analogRead(PIEZO_SENSOR);
    int sensorValue = analogRead(GAS_SENSOR);
    sensorV = (float)sensorValue/1024*5.0;
    gas = (5.0-sensorV)/sensorV;
    ratio = gas/calibratedGas;
    Serial.println(String(lumen) +";"+ String(motion) +";"+ String(sound) +";"+ String(piezo)+";"+ String(gas)+";"+ String(ratio));
  }
}
