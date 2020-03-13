/*
M-maxspeed:120?
N-maxspeed:450
minspeed:3200
Turns:14 approximately
*/

void Y_acc(word Y_Micro,boolean dir){//順轉  -頭朝下則逆轉:向後，逆轉  -頭朝下則順轉:向前
  digitalWrite(Y_DIR,dir);
  digitalWrite(YY_DIR,dir);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      delayMicroseconds(Micro);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      delayMicroseconds(Micro);
      if (digitalRead(Y_LIMIT) == HIGH){
        Serial.println("Arrival"); 
        delay(1000);
        break; 
      }
    }
  }
} 
void X_acc(word Micro,boolean dir){//順轉  -頭朝下則逆轉:向右，逆轉  -頭朝下則順轉:向左
  digitalWrite(X_DIR,dir);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(X_STP, HIGH);
      delayMicroseconds(Micro);
      digitalWrite(X_STP, LOW);
      delayMicroseconds(Micro);
      if (digitalRead(X_LIMIT) == HIGH){
        Serial.println("Arrival"); 
        delay(1000);
        break; 
      }
    }
  }
}
void Diagonally_acc(word Micro,boolean Y_dir,boolean X_dir) {
  digitalWrite(X_DIR, X_dir);  //true:右，false:左
  digitalWrite(Y_DIR, Y_dir);  //true:上，false:下
  digitalWrite(YY_DIR, Y_dir); 
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(X_STP,HIGH);
      digitalWrite(Y_STP, HIGH);
      digitalWrite(YY_STP,HIGH);
      delayMicroseconds(Micro);
      digitalWrite(X_STP,LOW);
      digitalWrite(Y_STP, LOW);
      digitalWrite(YY_STP,LOW);
      delayMicroseconds(Micro);
      if (digitalRead(Y_LIMIT) == HIGH || digitalRead(X_LIMIT) == HIGH){
        Serial.println("Arrival");
        delay(1000);
        break;
      }
    }
  }
}
