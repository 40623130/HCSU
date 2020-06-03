defineTaskLoop(Task1) {
  vrx_data = analogRead(vrx);//Read joystick_x
  x_a = ((-3.170055033245540e-09*vrx_data) -7.946250149636110e-04)*(vrx_data-1013)*(vrx_data-10)+150;//To cpurt the X_speed's equation
  if (vrx_data > 494 && vrx_data < 530){   //Range = 1023 於512為中點
    ;
  }
  else if (vrx_data > 530){
    X_acc(x_a,false,stps);  //Run by joystick
    Moter_S = 0;
  }
  else if (vrx_data < 494){
    X_acc(x_a,true,stps);   //Run by joystick
    Moter_S = 0;
  }
}
