#define EN 8      //步進馬達使能端
#define Y_DIR 6   //y軸 步進馬達方向控制
#define Y_STP 3   //y軸 步進控制
#define Y_LIMIT 10  //y軸 極限開關
int stps = 10000;
String str;

void setup() {
  Serial.begin(115200);
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(Y_LIMIT, INPUT);
  digitalWrite(EN, LOW);
}

void loop() {
  if (Serial.available()){
    str = Serial.readStringUntil('\n');
    if (str == "Push"){
      Y_acc(600,false);
      Serial.println("Pushing");
    }
    else if (str == "Back"){
      Y_acc(600,true);
      Serial.println("Going back");
    }
  }
}

void Y_acc(word Micro,boolean dir){//順轉  -頭朝下則逆轉:向右，逆轉  -頭朝下則順轉:向左
  digitalWrite(Y_DIR,dir);
  for (long int i = 0; i < stps; i++){
    if (i%3 ==0) {
      digitalWrite(Y_STP, HIGH);
      delayMicroseconds(Micro);
      digitalWrite(Y_STP, LOW);
      delayMicroseconds(Micro);
      if (digitalRead(Y_LIMIT) == HIGH){
        Serial.println("Arrival"); 
        delay(1000);
        break; 
      }
    }
  }
}
