#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>
 
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
//#define HARDWARE_TYPE MD_MAX72XX::GENERIC_HW
 
#define MAX_DEVICES 4
#define CS_PIN 10
 
MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);
 
void setup() {
 
  myDisplay.begin();
  myDisplay.setIntensity(4);
  myDisplay.displayClear();
  myDisplay.displayScroll("How To Electronics", PA_CENTER, PA_SCROLL_LEFT, 200);
}
 
void loop() {
  if (myDisplay.displayAnimate()) {
    myDisplay.displayReset();
  }
}