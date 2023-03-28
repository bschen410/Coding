#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
const int led=13;    //LED連接至數位接腳13。
const int sig=2;    //PING)))連接至數位接腳2。
const int speaker=11;

void setup() { 
    Serial.begin(9600);   //初始化串列埠，設定鮑率9600bps。
    pinMode(led,OUTPUT);    //設定數位接腳13為輸出模式。
    digitalWrite(led,LOW);   //關閉led。
    lcd.init();
    lcd.backlight();
}

void loop() {
    unsigned long cm;   //距離(單位:公分)。
    pinMode(sig,OUTPUT);    //設定數位接腳2為輸出模式。
    cm=ping(sig);   //讀取物體距離。
    Serial.print("distance=");    //顯示"distance="字元。
    Serial.print(cm);   //顯示物體距離。
    Serial.println("cm");   //顯示"cm"字元。
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("distance=");
    lcd.print(cm);
    lcd.print("cm");
    digitalWrite(led,HIGH);   //距離愈近，LED閃爍速度愈快。
    tone(speaker, 1000);
    delay(cm*10);
    digitalWrite(led, LOW);
    noTone(speaker);
    delay(cm*10);
}

int ping(int sig)
{
    unsigned long cm;     //距離(單位:公分)。
    unsigned long duration;   //脈寬(單位:微秒)。
    pinMode(sig,OUTPUT);    //設定數位接腳2為輸出模式。
    digitalWrite(sig,LOW);    //輸出脈寬5s的脈波啟動PING)))。
    delayMicroseconds(2);
    digitalWrite(sig,HIGH);
    delayMicroseconds(5);
    digitalWrite(sig,LOW);
    pinMode(sig,INPUT);   //設定數位接腳2為輸入模式。
    duration=pulseIn(sig,HIGH);   //讀取與物體距離成正比的脈波HIGH時間。
    cm=duration/29/2;   //計算物體距離(單位:公分)。
    if (cm > 100)
      return 101;
    return cm;      //傳回物體距離(單位:公分)
}

