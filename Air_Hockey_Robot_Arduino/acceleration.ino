void X_run(boolean dir){
  switch(X_state){
    case 0:
      for (word i = 540;i > 120;i--){
        X_acc(i,dir,10);
        if (i == 121){
          X_state = 1;
        }
      }
      break;
    case 1:
      do {
        X_acc(130,dir,60);
      }while(str != "Closer");
      for (word i = 130;i < 190;i++){
        X_acc(i,dir,5);
        if (i == 199){
          X_state = 2;
        }
      }
      break;
    case 2:
      for (word i = 190;i < 430;i++){
        X_acc(i,dir,5);
      }
      X_state = 3;
    default:
      X_state = 3;
  }
}

/*
void Y_acc(boolean dir){
  switch(Y_state){
    case 0:
      for (word i = 540;i > 120;i--){
        Y_acc(i,dir,5);
        if (i == 121){
          Y_state = 1;
        }
      }
      break;
    case 1:
      do {
        Y_acc(130,dir,60);
      }while(str == "Closer");
      for (word i = 130;i < 200;i++){
        Y_acc(i,dir,5);
      }
      Y_state = 2;
      break;
    case 2:
      for (word i = 200;i < 440;i++){
        Y_acc(i,dir,5);
      }
      Y_state = 3;
    default:
      Y_state = 3;
  }
}

*/
