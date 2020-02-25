#include "Configuration.h"


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    // 讀取傳入的字元值
    while ((chr = Serial.read()) != '\n') {
      // 確認輸入的字元介於'0'和'9'，且索引i小於3（確保僅讀取前三個字）
      if (chr >= '0' && chr < = '9' && i < 3) {
      data[i] = chr;
      i++;
      }
    }
  }
}
