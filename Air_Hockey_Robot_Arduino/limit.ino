void limit() {
  if(digitalRead(X_LIMIT) == HIGH){
    X_state = 3;
  }
  else if(digitalRead(Y_LIMIT) == HIGH){
    Y_state = 3;
  }
}
