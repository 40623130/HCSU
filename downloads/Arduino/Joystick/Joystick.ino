#include "SCoop.h"
#define X_STP 2
#define Y_STP 3
#define YY_STP 4
#define X_DIR 5
#define Y_DIR 6
#define YY_DIR 7
#define EN 8
#define X_LIMIT 9
#define Y_LIMIT 10  
#define vrx A0 // joystick-Abort
#define vry A1 //-Hold
int vrx_data = 0; 
int vry_data = 0; 
int x_a = 0;
int y_a = 0; 
int stps = 3;
 
void setup() {
  pinMode(vrx,INPUT); 
  pinMode(vry,INPUT);
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(YY_DIR, OUTPUT);
  pinMode(YY_STP, OUTPUT);
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(X_LIMIT, INPUT);
  pinMode(Y_LIMIT, INPUT);
  digitalWrite(EN, LOW);
  Serial.begin(115200);
  mySCoop.start();
}

void loop(){  
  yield();
  vrx_data = analogRead(vrx);
  x_a = ((-0.00000001347273389130310*vrx_data) -0.003377156313595)*(vrx_data-1013)*(vrx_data-10)+150;
  if (digitalRead(X_LIMIT) == LOW){
    if (vrx_data > 494 && vrx_data < 530){//Range = 1023 於512為中點
      ;
    }
    else if (vrx_data > 530){
      X_acc(x_a,false);
    }
    else if (vrx_data < 494){
      X_acc(x_a,true);
    }
  }
}
defineTaskLoop(Task1) {
  vry_data = analogRead(vry);
  y_a = ((-5.943853187337017e-09*vry_data) -0.001489921903057)*(vry_data-1013)*(vry_data-10)+150;
  if (digitalRead(X_LIMIT) == LOW){
    if (vry_data > 494 && vry_data < 530){//Range = 1023 於512為中點
      ;
    }
    else if (vry_data > 530){
      Y_acc(y_a,true);
    }
    else if (vry_data < 494){
      Y_acc(y_a,false);
    }
  }
}

void X_acc(word Micro,boolean dir){
  digitalWrite(X_DIR,dir);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(X_STP, HIGH);
      delayMicroseconds(Micro);
      digitalWrite(X_STP, LOW);
      delayMicroseconds(Micro);
    }
  }
}

void Y_acc(word Micro,boolean dir){
  digitalWrite(Y_DIR,dir);
  digitalWrite(YY_DIR,dir);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      delayMicroseconds(Micro);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      delayMicroseconds(Micro);
    }
  }
}
