void step(boolean dir, byte dirPin, byte stepperPin, long int stps){
  digitalWrite(dirPin, dir);
  delay(100);
  for (long int i = 0; i < stps; i++) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(600);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(600);
    if (digitalRead(X_LIMIT) == HIGH || digitalRead(Y_LIMIT) == HIGH){
      break;
    }
  }
}

void YYY_step_false(){
  step(false, Y_DIR, Y_STP, stps);
  step(false, YY_DIR, YY_STP, stps);
}
void YYY_step_true(){
  step(true, YY_DIR, YY_STP, stps);
  step(true, Y_DIR, Y_STP, stps);
}      
void YYY_limit_step_false(){
  step(false, Y_DIR, Y_STP, limit_stps);
  step(false, YY_DIR, YY_STP, limit_stps);
}
void YYY_limit_step_true(){
  step(true, YY_DIR, YY_STP, limit_stps);
  step(true, Y_DIR, Y_STP, limit_stps);
}
void Diagonally_left_up(){
  step(true, X_DIR, X_STP, stps);
  YYY_limit_step_false();
}
void Diagonally_left_down(){
  step(false, X_DIR, X_STP, stps);
  YYY_limit_step_false();
}
void Diagonally_right_up(){
  step(true, X_DIR, X_STP, stps);
  YYY_limit_step_true();
}
void Diagonally_right_down(){
  step(false, X_DIR, X_STP, stps);
  YYY_limit_step_true();
}
        
