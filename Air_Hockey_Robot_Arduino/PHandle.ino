defineTaskLoop(Task1) {
  vrx_data = analogRead(vrx);//Read joystick_x
  x_a = ((-3.170055033245540e-09*vrx_data) -7.946250149636110e-04)*(vrx_data-1013)*(vrx_data-10)+150;//To cpurt the X_speed's equation
  if (vrx_data > 494 && vrx_data < 530){   //Range = 1023 於512為中點
    if (Serial.available()){
      str = Serial.readStringUntil('\n');
      if (str == "RIGHT"){
        X_acc(200,true,stps);
      }
      else if (str == "LEFT"){
        X_acc(200,false,stps);
      }
      str = "";
    }
  }
  else if (vrx_data > 530){
    str = "";
    X_acc(x_a,false,stps);  //Run by joystick
  }
  else if (vrx_data < 494){
    str = "";
    X_acc(x_a,true,stps);   //Run by joystick
  }
}
