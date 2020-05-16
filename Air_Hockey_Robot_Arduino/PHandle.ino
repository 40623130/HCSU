defineTaskLoop(Task1) {
  vrx_data = analogRead(vrx);//Read joystick_x
  x_a = ((-3.170055033245540e-09*vrx_data) -7.946250149636110e-04)*(vrx_data-1013)*(vrx_data-10)+150;//To cpurt the X_speed's equation
  if (vrx_data > 494 && vrx_data < 530){   //Range = 1023 於512為中點
    while(!Serial.available()) {
      delay(2);
    }
    while (Serial.available()){
      delay(2);
      if (readString == "RIGHT"){
        X_Motor_s = true;
      }
      else if (readString == "LEFT"){
        X_Motor_s = false;
      }
      delay(2);
      if (Serial.available() >0){
        char T = Serial.read();  //gets one byte from serial buffer
        readString += T;         //makes the string readString
        if (X_Motor_s == true){
          X_acc(T,true);
        }
        else if (X_Motor_s == false){
          X_acc(T,false);
        }
      }
      delay(2);
      readString = "";
    }
    /*if (readString.length() >0){  //Use to repaire
      Serial.print("Arduino received: ");  
      Serial.println(readString); //see what was received
      readString = "";
    }*/
  }
  else if (vrx_data > 530){
    readString = "";
    X_acc(x_a,false);  //Run by joystick
  }
  else if (vrx_data < 494){
    readString = "";
    X_acc(x_a,true);   //Run by joystick
  }
}

defineTaskLoop(Task2) {
  vry_data = analogRead(vry);//Read joystick_y
  y_a = ((-3.170055033245540e-09*vry_data) -7.946250149636110e-04)*(vry_data-1013)*(vry_data-10)+150;//To cpurt the Y_speed's equation
  if (vry_data > 494 && vry_data < 530){//Range = 1023 於512為中點
    ;
  }
  else if (vry_data > 530){
    readString = "";
    Y_acc(y_a,true);   //Run by joystick
  }
  else if (vry_data < 494){
    readString = "";
    Y_acc(y_a,false);  //Run by joystick
  }
}
