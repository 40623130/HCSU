void X_limit() {
  if(digitalRead(X_LIMIT_R) == HIGH){
    Limit_Situasion = 1;
    delay(10);
  }
  if(digitalRead(X_LIMIT_L) == HIGH){
    Limit_Situasion = 2;
    delay(10);
  }
}

void Limit(){
  if(Limit_Situasion == 1){
    X_acc(300,false,1000);
    delay(10);
    Limit_Situasion = 0;
  }
  else if(Limit_Situasion == 2){
    X_acc(300,true,1000);
    delay(10);
    Limit_Situasion = 0;
  }
}
