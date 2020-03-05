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
    limit();
    if (str == "Push"){
      YYY_step_true();
      Serial.println("Push");
    }
    else if (str == "Back"){
      YYY_step_false();
      Serial.println("Back");
    }
    if (str == "Right"){
      step(true, X_DIR, X_STP, stps);
      Serial.println("Right");
    } 
    else if (str == "Back"){
      step(false, X_DIR, X_STP, stps);
      Serial.println("Back");
    }
    if (str == "Diagonally_left_down"){
      Diagonally_left_down();
      Serial.println("Diagonally_left_down");
    } 
    else if (str == "Diagonally_right_down"){
      Diagonally_right_down();
      Serial.println("Diagonally_right_down");
    }
    else if (str == "Diagonally_left_up"){
      Diagonally_left_up();
      Serial.println("Diagonally_left_up");
    } 
    else if (str == "Diagonally_right_up"){
      Diagonally_right_up();
      Serial.println("Diagonally_right_up");
    }
  }
}
