#define EN 8      //步進馬達使能端
#define Y_DIR 6   //y軸 步進馬達方向控制
#define YY_DIR 7  //y軸 步進馬達方向控制
#define Y_STP 3   //y軸 步進控制
#define YY_STP 4  //y軸 步進控制
#define Y_LIMIT 10  //y軸 極限開關
int state = 0;

void setup() {
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(YY_DIR, OUTPUT);
  pinMode(YY_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(Y_LIMIT, INPUT);
  digitalWrite(EN, LOW);
  Serial.begin(115200);
}

void loop() {
  switch(state){
    case 0:
      for (word i = 540;i > 120;i--){
        acc(i,true,5);
        if (i == 121){
          state = 1;
        }
      }
      break;
    case 1:
      do {
        acc(130,true,60);
      }while(digitalRead(Y_LIMIT) == LOW);
      for (word i = 130;i < 200;i++){
        acc(i,true,10);
        if (i == 199){
          state = 3;
        }
      }
      break;
    case 2:
      for (word i = 200;i < 440;i++){
        acc(i,true,10);
      }
      state = 3;
    default:
      state = 3;
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
