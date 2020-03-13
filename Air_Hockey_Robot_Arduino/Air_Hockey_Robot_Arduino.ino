#include "Configuration.h"

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

void loop() {
  if (Serial.available()){
    str = Serial.readStringUntil('\n');
    if (str == "Push"){
      Y_step_true();
      Serial.println("Push");
    }
  }
}
