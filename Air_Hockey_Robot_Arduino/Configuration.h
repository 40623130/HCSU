#include "SCoop.h"
#define EN 8       //步進馬達使能端
#define X_DIR 5    //X軸 步進馬達方向控制
#define Y_DIR 6    //y軸 步進馬達方向控制
#define YY_DIR 7   //y軸 步進馬達方向控制
#define X_STP 2    //x軸 步進控制
#define Y_STP 3    //y軸 步進控制
#define YY_STP 4   //y軸 步進控制
#define X_LIMIT_S 9  //x軸 極限開關
#define Y_LIMIT_S 10 //y軸 極限開關
#define vrx A0     //joystick-Abort
#define vry A1     //coolEn

int X_state = 0;
int Y_state = 0;
int vrx_data = 0; 
int vry_data = 0;
boolean X_Motor_s;
boolean Y_Motor_s;
String readString;
int x_a = 0;
int y_a = 0; 
int stps = 3;

void setup() {
  mySCoop.start();
  Serial.begin(115200);
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(YY_DIR, OUTPUT);
  pinMode(YY_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(X_LIMIT_S, INPUT);
  pinMode(Y_LIMIT_S, INPUT);
  digitalWrite(EN, LOW);
}
