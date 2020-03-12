#define EN 8      //步進馬達使能端
#define Y_DIR 6   //y軸 步進馬達方向控制
#define YY_DIR 7  //y軸 步進馬達方向控制
#define Y_STP 3   //y軸 步進控制
#define YY_STP 4  //y軸 步進控制
#define Y_LIMIT 10  //y軸 極限開關
int state = 1;
int stps = 1000;

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
  if (digitalRead(Y_LIMIT) == HIGH){
    delay(5000);
  }
  else if (digitalRead(Y_LIMIT) == LOW){
    acc(1500,true);
    acc(1500,false);
    acc(1000,true);
    acc(1000,false);
    acc(900,true);
    acc(800,true);
    acc(700,true);
    acc(600,true);
    acc(500,true);
    acc(450,true);
    acc(400,true);
    acc(350,true);
    acc(320,true);
    acc(270,true);
    acc(260,true);
    acc(210,true);
    acc(160,true);
    acc(110,true);
  }
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
        delay(1000);
        break; 
      }
    }
  }
} 
