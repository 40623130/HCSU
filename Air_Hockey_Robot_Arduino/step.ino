/*
M-maxspeed:200?
N-maxspeed:450
minspeed:3200

void step(boolean dir1, byte dirPin1, boolean dir2, byte dirPin2, boolean dir3, byte dirPin3, byte stepperPin1, byte stepperPin2, byte stepperPin3 , long int stps){
  digitalWrite(dirPin1, dir1);
  digitalWrite(dirPin2, dir2);
  digitalWrite(dirPin3, dir3);
  delay(100);
  for (long int i = 0; i < stps; i++) {
    digitalWrite(stepperPin1, HIGH);
    digitalWrite(stepperPin2, HIGH);
    digitalWrite(stepperPin3, HIGH);
    delayMicroseconds(600);
    digitalWrite(stepperPin1, LOW);
    digitalWrite(stepperPin2, LOW);
    digitalWrite(stepperPin3, LOW);
    delayMicroseconds(600);
    if (digitalRead(X_LIMIT) == HIGH || digitalRead(Y_LIMIT) == HIGH){
      break;
    }
  }
}
*/

void X_step_right() {       //順轉  -頭朝下則逆轉:向右
  digitalWrite(X_DIR, true);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(X_STP, HIGH);
      delayMicroseconds(600);
      digitalWrite(X_STP, LOW);
      delayMicroseconds(600);
      if (digitalRead(X_LIMIT) == HIGH){
        Serial.println("已到達最左端");
        delay(10);
        break;
      }
    }
  }
}
void X_step_left() {       //順轉  -頭朝下則逆轉:向左
  digitalWrite(X_DIR, false);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(X_STP, HIGH);
      delayMicroseconds(600);
      digitalWrite(X_STP, LOW);
      delayMicroseconds(600);
      if (digitalRead(X_LIMIT) == HIGH){
        Serial.println("已到達最右端");
        delay(10);
        break;
      }
    }
  }
}
void Y_step_back() {       //順轉  -頭朝下則逆轉:向後
  digitalWrite(Y_DIR, false);
  digitalWrite(YY_DIR, false);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      delayMicroseconds(600);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      delayMicroseconds(600);
      if (digitalRead(Y_LIMIT) == HIGH){
        Serial.println("已退到最底部");
        delay(10);
        break;
      }
    }
  }
}
void Y_step_front() {        //逆轉  -頭朝下則順轉:向前
  digitalWrite(Y_DIR, true);
  digitalWrite(YY_DIR, true);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      delayMicroseconds(600);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      delayMicroseconds(600);
      if (digitalRead(Y_LIMIT) == HIGH){
        Serial.println("已進到最前端"); //前端，無安裝極限開關無法測達極限位置
        delay(10);
        break;
      }
    }
  }
}
void Diagonally_right_front() {        //逆轉:向右  -頭朝下則順轉:向前
  digitalWrite(Y_DIR, true);
  digitalWrite(YY_DIR, true);
  digitalWrite(X_DIR, true);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      digitalWrite(X_STP,HIGH);
      delayMicroseconds(600);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      digitalWrite(X_STP,LOW);
      delayMicroseconds(600);
      if (digitalRead(Y_LIMIT) == HIGH || digitalRead(X_LIMIT) == HIGH){
        Serial.println("已到右前端"); //前端，無安裝極限開關無法測達極限位置
        delay(10);
        break;
      }
    }
  }
}
void Diagonally_right_back(){        //逆轉:向右  -頭朝下則逆轉:向後
  digitalWrite(Y_DIR, false);
  digitalWrite(YY_DIR, false);
  digitalWrite(X_DIR, true);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      digitalWrite(X_STP,HIGH);
      delayMicroseconds(600);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      digitalWrite(X_STP,LOW);
      delayMicroseconds(600);
      if (digitalRead(Y_LIMIT) == HIGH || digitalRead(X_LIMIT) == HIGH){
        Serial.println("已到右後端");
        delay(10);
        break;
      }
    }
  }
}
void Diagonally_left_front(){        //正轉:向左  -頭朝下則順轉:向前
  digitalWrite(Y_DIR, true);
  digitalWrite(YY_DIR, true);
  digitalWrite(X_DIR, false);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      digitalWrite(X_STP,HIGH);
      delayMicroseconds(600);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      digitalWrite(X_STP,LOW);
      delayMicroseconds(600);
      if (digitalRead(Y_LIMIT) == HIGH || digitalRead(X_LIMIT) == HIGH){
        Serial.println("已到左前端");//前端，無安裝極限開關無法測達極限位置
        delay(10);
        break;
      }
    }
  }
}
void Diagonally_left_back(){        //正轉:向左  -頭朝下則逆轉:向後
  digitalWrite(Y_DIR, false);
  digitalWrite(YY_DIR, false);
  digitalWrite(X_DIR, false);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      digitalWrite(X_STP,HIGH);
      delayMicroseconds(600);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      digitalWrite(X_STP,LOW);
      delayMicroseconds(600);
      if (digitalRead(Y_LIMIT) == HIGH || digitalRead(X_LIMIT) == HIGH){
        Serial.println("已到左後端");
        delay(10);
        break;
      }
    }
  }
}
