#include <Servo.h>
Servo myservoL, myservoR;

const byte ServoR_pin = 12;
const byte ServoL_pin = 13;

char command = 'S';
char prevCommand = 'A';
unsigned long timer0 = 2000;  // Stores the time (in millis since execution started)
unsigned long timer1 = 0;     // Stores the time when the last command was received from the phone

void setup() {
    myservoR.attach(ServoR_pin);
    myservoL.attach(ServoL_pin);

    myservoR.write(90);  // 左右停止
    myservoL.write(90);

    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        // timer1 = millis();
        prevCommand = command;
        command = Serial.read();
        // Change pin mode only if new command is different from previous.
        if (command != prevCommand) {
            // Serial.println(command);
            switch (command) {
                case 'F':  // 直行，右順左逆
                    myservoR.write(0);
                    myservoL.write(180);
                    break;
                case 'B':  // 後退，左順右逆
                    myservoR.write(180);
                    myservoL.write(0);
                    break;
                case 'L':  // 左轉
                    myservoR.write(0);
                    myservoL.write(90);
                    break;
                case 'R':  // 右轉
                    myservoR.write(90);
                    myservoL.write(180);
                    break;
                case 'S':  // 左右停止
                    myservoR.write(90);
                    myservoL.write(90);
                    break;
            }
            delay(100);
        }
    }
}
