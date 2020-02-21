#define GREEN 2
#define BLUE 4
String str;

void setup() {
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  Serial.begin(9600);
}
 
void loop() {
  if (Serial.available()) {
    // 讀取傳入的字串直到"\n"結尾
    str = Serial.readStringUntil('\n');
 
    if (str == "GREEN_ON") {           // if str is  "GREEN_ON" open the light
        digitalWrite(GREEN, HIGH);
        Serial.println("GREEN is ON");
    } else if (str == "GREEN_OFF") {  // if str is  "GREEN_OFF" open the light
        digitalWrite(GREEN, LOW);
        Serial.println("GREEN is OFF");
    }
    if (str == "BLUE_ON") {           // 若字串值是 "LED_ON" 開燈
        digitalWrite(BLUE, HIGH);     // 開燈
        Serial.println("BLUE is ON"); // 回應訊息給電腦
    } else if (str == "BLUE_OFF") {
        digitalWrite(BLUE, LOW);
        Serial.println("BLUE is OFF");
    }
  }
}
