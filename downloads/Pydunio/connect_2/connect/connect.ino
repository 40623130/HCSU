#define LEFT 2
#define RIGHT 4
#define CHECK 7
String str;

void setup() {
  pinMode(LEFT, OUTPUT);
  pinMode(RIGHT, OUTPUT);
  pinMode(CHECK, OUTPUT);
  Serial.begin(9600);
}
 
void loop() {
  if (Serial.available()) {
    // 讀取傳入的字串直到"\n"結尾
    str = Serial.readStringUntil('\n');
 
    if (str == "LEFT_ON") {           // if str is  "GREEN_ON" open the light
        digitalWrite(LEFT, HIGH);
        Serial.println("LEFT is ON");
    } else if (str == "LEFT_OFF") {  // if str is  "GREEN_OFF" open the light
        digitalWrite(LEFT, LOW);
        Serial.println("LEFT is OFF");
    }
    
    if (str == "RIGHT_ON") {           // 若字串值是 "LED_ON" 開燈
        digitalWrite(RIGHT, HIGH);     // 開燈
        Serial.println("RIGHT is ON"); // 回應訊息給電腦
    } else if (str == "RIGHT_OFF") {
        digitalWrite(RIGHT, LOW);
        Serial.println("RIGHT is OFF");
    }
    
    if (str == "CHECK_ON") {           // 若字串值是 "LED_ON" 開燈
        digitalWrite(CHECK, HIGH);     // 開燈
        Serial.println("CHECK is ON"); // 回應訊息給電腦
    } else if (str == "CHECK_OFF") {
        digitalWrite(CHECK, LOW);
        Serial.println("CHECK is OFF");
    }
  }
}
