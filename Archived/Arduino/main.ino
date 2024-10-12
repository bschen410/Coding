#include <MD_MAX72xx.h>
#include <MD_Parola.h>
#include <SPI.h>
#include <SdFat.h>
#include <Servo.h>

#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 4
#define CS_PIN 10

SdFat sd;
Servo myservoL, myservoR;
MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

const byte ServoR_pin = 12;
const byte ServoL_pin = 13;

const uint8_t volume = 0;     // MP3 Player volume 0=max, 255=lowest (off)
const uint16_t monoMode = 1;  // Mono setting 0=off, 3=max

#define TRIGGER_COUNT 9
int triggerPins[TRIGGER_COUNT] = {0, 1, 5, 10, A0, A1, A2, A3, A4};
int stopPin = A5;     // This pin triggers a track stop.
int lastTrigger = 0;  // This variable keeps track of which tune is playing

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

    for (int i = 0; i < TRIGGER_COUNT; i++) {
        pinMode(triggerPins[i], INPUT_PULLUP);
    }
    pinMode(stopPin, INPUT_PULLUP);

    initSD();         // Initialize the SD card
    initMP3Player();  // Initialize the MP3 Shield

    myDisplay.begin();
    myDisplay.setIntensity(4);
    myDisplay.displayClear();
    myDisplay.displayScroll("BANANA!", PA_CENTER, PA_SCROLL_LEFT, 200);
}

void loop() {
    if (myDisplay.displayAnimate()) {
        myDisplay.displayReset();
    }
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
    for (int i = 0; i < TRIGGER_COUNT; i++) {
        if ((digitalRead(triggerPins[i]) == LOW) && ((i + 1) != lastTrigger)) {
            lastTrigger = i + 1;  // Update lastTrigger variable to current trigger
            /* If another track is playing, stop it: */
            if (MP3player.isPlaying())
                MP3player.stopTrack();

            /* Use the playTrack function to play a numbered track: */
            uint8_t result = MP3player.playTrack(lastTrigger);
            // An alternative here would be to use the
            //  playMP3(fileName) function, as long as you mapped
            //  the file names to trigger pins.

            if (result == 0)  // playTrack() returns 0 on success
            {
                // Success
            } else  // Otherwise there's an error, check the code
            {
                // Print error code somehow, someway
            }
        }
    }
    // After looping through and checking trigger pins, check to
    //  see if the stopPin (A5) is triggered.
    if (digitalRead(stopPin) == LOW) {
        lastTrigger = 0;  // Reset lastTrigger
        // If another track is playing, stop it.
        if (MP3player.isPlaying())
            MP3player.stopTrack();
    }
}

void initSD() {
    // Initialize the SdCard.
    if (!sd.begin(SD_SEL, SPI_HALF_SPEED))
        sd.initErrorHalt();
    if (!sd.chdir("/"))
        sd.errorHalt("sd.chdir");
}

void initMP3Player() {
    uint8_t result = MP3player.begin();  // init the mp3 player shield
    if (result != 0)                     // check result, see readme for error codes.
    {
        // Error checking can go here!
    }
    MP3player.setVolume(volume, volume);
    MP3player.setMonoMode(monoMode);
}