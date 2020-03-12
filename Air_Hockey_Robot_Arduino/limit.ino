/*
void limit() {
  if(digitalRead(X_LIMIT) == LOW){
    switch(X_state){
      case 0:
        Serial.println("LOW and X_state=0");
        //step(true, X_DIR, X_STP, stps);
        break;
      case 1:
        Serial.println("LOW and X_state=1");
        //step(false, X_DIR, X_STP, stps);
        break;
      default:
        Serial.println("LOW");
    }
  }
  else if(digitalRead(X_LIMIT) == HIGH){
    switch(X_state){
      case 0:
        Serial.println("HIGH and X_state=0");
        step(false, X_DIR, X_STP, limit_stps);
        X_state = 1;
        break;
      case 1:
        Serial.println("HIGH and X_state=1");
        step(true, X_DIR, X_STP, limit_stps);
        X_state = 0;
        break;
      default:
        Serial.println("HIGH");
    }
  }
  else if(digitalRead(Y_LIMIT) == LOW){
    switch(Y_state){
      case 0:
        Serial.println("LOW and Y_state=0");
        //YYY_step_true();
        break;
      case 1:
        Serial.println("LOW and Y_state=1");
        //YYY_step_false();
        break;
      default:
        Serial.println("LOW");
    }
  }
  else if(digitalRead(Y_LIMIT) == HIGH){
    switch(Y_state){
      case 0:
        Serial.println("HIGH and Y_state=0");
        YYY_limit_step_false();
        Y_state = 1;
        break;
      case 1:
        Serial.println("HIGH and Y_state=1");
        YYY_limit_step_true();
        Y_state = 0;
        break;
      default:
        Serial.println("HIGH");
    }
  }
}
*/
