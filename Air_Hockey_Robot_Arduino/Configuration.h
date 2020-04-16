#define EN 8      //步進馬達使能端
#define X_DIR 5   //X軸 步進馬達方向控制
#define Y_DIR 6   //y軸 步進馬達方向控制
#define YY_DIR 7  //y軸 步進馬達方向控制
#define X_STP 2   //x軸 步進控制
#define Y_STP 3   //y軸 步進控制
#define YY_STP 4  //y軸 步進控制
#define X_LIMIT 9  //x軸 極限開關
#define Y_LIMIT 10  //y軸 極限開關

int X_state = 0;
int Y_state = 0;
word Micro;
String str;

void setup() {
  Serial.begin(115200);
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(YY_DIR, OUTPUT);
  pinMode(YY_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(X_LIMIT, INPUT);
  pinMode(Y_LIMIT, INPUT);
  digitalWrite(EN, LOW);
}
