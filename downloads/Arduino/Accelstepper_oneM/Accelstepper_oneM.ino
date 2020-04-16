#include <AccelStepper.h>
#define EN 8
#define X_STP 2
#define X_DIR 5
#define X_LIMIT 9
AccelStepper X_motor(1, X_STP, X_DIR);
int state = 0;

void setup() {
  X_motor.setEnablePin(EN);
  X_motor.setMaxSpeed(20000);     //設置最大速度
  //X_motor.setAcceleration(10000);  //設置加速度
  X_motor.setSpeed(3000);         //設置初速度
  X_motor.move(200);
  pinMode(EN, OUTPUT);
  pinMode(X_LIMIT, INPUT);
  digitalWrite(EN, LOW);
  Serial.begin(115200);
  X_motor.enableOutputs();
}

void loop() {  
  if (digitalRead(X_LIMIT) == LOW){
    //X_motor.run();                //步進電機運行-先加速後減速模式
    X_motor.runSpeed();           //步進電機運行-勻速模式
    //X_motor.move(1000);           //相對目標位置
    //X_motor.moveTo(1000);         //絕對目標位置
  }
  else{
    X_motor.stop();
  }
}
