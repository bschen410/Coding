#include <SPI.h>           // SPI library
#include <SdFat.h>         // SDFat Library
//#include <SdFatUtil.h>     // SDFat Util Library
#include <SFEMP3Shield.h>  // Mp3 Shield Library

SdFat sd; // Create object to handle SD functions

SFEMP3Shield MP3player; // Create Mp3 library object
// These variables are used in the MP3 initialization to set up
// some stereo options:
const uint8_t volume = 0; // MP3 Player volume 0=max, 255=lowest (off)
const uint16_t monoMode = 1;  // Mono setting 0=off, 3=max

/* Pin setup */
#define TRIGGER_COUNT 9
int triggerPins[TRIGGER_COUNT] = {0, 1, 5, 10, A0, A1, A2, A3, A4};
int stopPin = A5; // This pin triggers a track stop.
int lastTrigger = 0; // This variable keeps track of which tune is playing

void setup()
{
  /* Set up all trigger pins as inputs, with pull-ups activated: */
  for (int i=0; i<TRIGGER_COUNT; i++)
  {
    pinMode(triggerPins[i], INPUT_PULLUP);
  }
  pinMode(stopPin, INPUT_PULLUP);

  initSD();  // Initialize the SD card
  initMP3Player(); // Initialize the MP3 Shield
}

// All the loop does is continuously step through the trigger
//  pins to see if one is pulled low. If it is, it'll stop any
//  currently playing track, and start playing a new one.
void loop()
{
  for (int i=0; i<TRIGGER_COUNT; i++)
  {
    if ((digitalRead(triggerPins[i]) == LOW) && ((i+1) != lastTrigger))
    {
      lastTrigger = i+1; // Update lastTrigger variable to current trigger
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
      }
      else // Otherwise there's an error, check the code
      {
        // Print error code somehow, someway
      }
    }
  }
  // After looping through and checking trigger pins, check to
  //  see if the stopPin (A5) is triggered.
  if (digitalRead(stopPin) == LOW)
  {
    lastTrigger = 0; // Reset lastTrigger
    // If another track is playing, stop it.
    if (MP3player.isPlaying())
      MP3player.stopTrack();
  }
}

// initSD() initializes the SD card and checks for an error.
void initSD()
{
  //Initialize the SdCard.
  if(!sd.begin(SD_SEL, SPI_HALF_SPEED)) 
    sd.initErrorHalt();
  if(!sd.chdir("/")) 
    sd.errorHalt("sd.chdir");
}

// initMP3Player() sets up all of the initialization for the
// MP3 Player Shield. It runs the begin() function, checks
// for errors, applies a patch if found, and sets the volume/
// stero mode.
void initMP3Player()
{
  uint8_t result = MP3player.begin(); // init the mp3 player shield
  if(result != 0) // check result, see readme for error codes.
  {
    // Error checking can go here!
  }
  MP3player.setVolume(volume, volume);
  MP3player.setMonoMode(monoMode);
}
