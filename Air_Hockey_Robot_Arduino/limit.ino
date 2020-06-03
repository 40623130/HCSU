void Limit() {
  if(digitalRead(X_LIMIT_R) == HIGH){
    Limit_Situasion = 1;
  }
  else if(digitalRead(X_LIMIT_L) == HIGH){
    Limit_Situasion = 2;
  }
  if(digitalRead(Y_LIMIT) == HIGH){
    Limit_Situasion = 3;
  }
}


void Limit_S(){
  if(Limit_Situasion == 1){
    X_acc(300,false,250);
    Limit_Situasion = 0;
  }
  else if(Limit_Situasion == 2){
    X_acc(300,true,250);
    Limit_Situasion = 0;
  }
  if (Limit_Situasion == 3){
    Y_acc(300,true,250);
    Limit_Situasion = 0;
  }
}
