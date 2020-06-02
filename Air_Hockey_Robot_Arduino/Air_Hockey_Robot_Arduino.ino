#include "Configuration.h"

void loop() {
  Limit();
  Limit_S();
  yield();
  
  vry_data = analogRead(vry);//Read joystick_y
  y_a = ((-5.943853187337017e-09*vry_data) -0.001489921903057)*(vry_data-1013)*(vry_data-10)+150;//To cpurt the Y_speed's equation
  if (vry_data > 494 && vry_data < 530){//Range = 1023 於512為中點
    if (Serial.available()){
      str = Serial.readStringUntil('\n');
      if (str == "PUSH"){
        Y_acc(200,true,stps);
      }
      else if (str == "BACK"){
        Y_acc(200,false,stps);
      }
      str = "";
    }
  }
  else if (vry_data > 530){
    str = "";
    Y_acc(y_a,true,stps);   //Run by joystick
  }
  else if (vry_data < 494){
    str = "";
    Y_acc(y_a,false,stps);  //Run by joystick
  }
}
