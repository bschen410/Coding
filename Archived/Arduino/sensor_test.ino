#include <Servo.h>
Servo myservoL,myservoR;

const byte ServoR_pin = 12;
const byte ServoL_pin = 13; 
const byte Sensor_R = 6;
const byte Sensor_C = 7;
const byte Sensor_L = 8;
boolean R,C,L,RR,LL;



void setup() 
{ 
  myservoR.attach(ServoR_pin);
  myservoL.attach(ServoL_pin);
  pinMode(Sensor_R,INPUT);
  pinMode(Sensor_C,INPUT);
  pinMode(Sensor_L,INPUT);
  Serial.begin(9600); 
} 
 
void loop() 
{
 
    R = digitalRead(Sensor_R);
    C = digitalRead(Sensor_C);
    L = digitalRead(Sensor_L);
    RR = digitalRead(9);
    LL = digitalRead(10);
    Serial.print(R);
    Serial.print(C);
    Serial.println(L);
    if (C == 0) {
      myservoR.write(0);
      myservoL.write(180);
    } else if (R == 0) {
      myservoR.write(90);
      myservoL.write(180);
    } else if (L == 0) {
      myservoR.write(0);
      myservoL.write(90);
    }
    if (R == 0 && C == 0 && L == 0 && RR == 0) {
      while (true) {
        myservoR.write(90);
        myservoL.write(90);
      }
    } else if (R == 0 && C == 0 && L == 0 && LL == 0) {
      while (true) {
        myservoR.write(90);
        myservoL.write(90);
      }
    }
    // delay(1000);
}
