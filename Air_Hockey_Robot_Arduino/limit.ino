void limit() {
  if(digitalRead(X_LIMIT) == LOW){
    X_state = 3;
  }
  else if(digitalRead(Y_LIMIT) == LOW){
    Y_state = 3;
  }
}
