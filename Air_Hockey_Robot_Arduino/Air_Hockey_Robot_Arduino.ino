#include "Configuration.h"

void loop() {
  Limit();
  Limit_S();
  yield();
  
  vry_data = analogRead(vry);//Read joystick_y
  y_a = ((-5.943853187337017e-09*vry_data) -0.001489921903057)*(vry_data-1013)*(vry_data-10)+150;//To cpurt the Y_speed's equation
  if (vry_data > 494 && vry_data < 530){//Range = 1023 於512為中點
    if (Serial.available()){
      readString = Serial.readStringUntil('\n');
      if (readString == "RIGHT"){
        Moter_S = 1;
      }
      else if (readString == "LEFT"){
        Moter_S = 2;
      }
      else if (readString == "PUSH"){
        Moter_S = 3;
      }
      else if (readString == "BACK"){
        Moter_S = 4;
      }
      else if (readString == "STOP"){
        Moter_S = 0;
      }
    }
    if(Moter_S == 0){
      X_acc(0,true,A_stps);
      Y_acc(0,false,A_stps);
    }
    else if(Moter_S == 1){
      X_acc(300,false,A_stps);
    }
    else if(Moter_S == 2){
      X_acc(300,true,A_stps);
    }
    else if(Moter_S == 3){
      Y_acc(300,true,A_stps);
    }
    else if(Moter_S == 4){
      Y_acc(300,false,A_stps);
    }
  }
  else if (vry_data > 530){
    Y_acc(y_a,true,stps);   //Run by joystick
    Moter_S = 0;
  }
  else if (vry_data < 494){
    Y_acc(y_a,false,stps);  //Run by joystick
    Moter_S = 0;
  }
}
