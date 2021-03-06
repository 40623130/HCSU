#define EN 8      //步進馬達使能端
#define Y_DIR 6   //y軸 步進馬達方向控制
#define YY_DIR 7  //y軸 步進馬達方向控制
#define Y_STP 3   //y軸 步進控制
#define YY_STP 4  //y軸 步進控制
#define Y_LIMIT 10  //y軸 極限開關
int Y_state = 1;
int stps = 10;
word Micro,Micro_read;

void setup() {
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(YY_DIR, OUTPUT);
  pinMode(YY_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(Y_LIMIT, INPUT);
  digitalWrite(EN, LOW);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  while(Serial.available()){
    Micro = Serial.parseInt();
    Micro_read = Serial.parseInt();
  }
  Serial.println(Micro_read);
  acc(Micro,true);
}

void acc(word Micro,boolean dir){
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
        Serial.println("HIGH");
        digitalWrite(Y_STP, HIGH);
        digitalWrite(YY_STP,HIGH);
        delayMicroseconds(0);
        digitalWrite(Y_STP, LOW);
        digitalWrite(YY_STP,LOW);
        delayMicroseconds(0);
        delay(1000);
        break;
      }
    }
  }
} 
