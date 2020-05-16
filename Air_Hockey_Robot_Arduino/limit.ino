void X_limit() {
  if(digitalRead(X_LIMIT_S) == LOW){
    if(X_Motor_s == true){
      X_acc(false,300,30);
    }
    else if(X_Motor_s == false){
      X_acc(true,300,30);
    }
  }
}

void Y_limit() {
  if(digitalRead(Y_LIMIT_S) == LOW){
    if(Y_Motor_s == true){
      Y_acc(false,300,1200);
    }
    else if(Y_Motor_s == false){
      Y_acc(true,300,30);
    }
  }
}
