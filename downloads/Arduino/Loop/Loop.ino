#define EN 8      //步進馬達使能端
#define Y_DIR 6   //y軸 步進馬達方向控制
#define YY_DIR 7  //y軸 步進馬達方向控制
#define Y_STP 3   //y軸 步進控制
#define YY_STP 4  //y軸 步進控制
#define Y_LIMIT 10  //y軸 極限開關
int state = 1;

void setup() {
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(YY_DIR, OUTPUT);
  pinMode(YY_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(Y_LIMIT, INPUT);
  digitalWrite(EN, LOW);
  Serial.begin(9600);
}

void loop() {
  if (state == 1){
    for (word i = 400;i < 600;i++){
      acc(i,true,10);
      if (digitalRead(Y_LIMIT) == LOW){
        delay(1000);
        break; 
      }
    }
    for (word i = 540;i > 120;i--){
      acc(i,true,5);
      Serial.println("Pushing");
      if (digitalRead(Y_LIMIT) == LOW){
        delay(1000);
        break; 
      }
      else if (i == 121){
        state = 2;
      }
    }
  }
  while (state == 2){
    acc(120,true,1200);
    if (digitalRead(Y_LIMIT) == LOW){
      delay(1000);
      state = 1;
      break; 
    }
  }
}


void acc(word Micro,boolean dir,word stps){
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
    }
  }
} 
