#include "Configuration.h"

void loop() {
  limit();
  if (Serial.available()){
    str = Serial.readStringUntil('\n');
    if (str == "RIGHT"){
      X_run(true);
      Serial.println("RIGHT");
    }
    else if(str == "LEFT"){
      X_run(false);
      Serial.println("LEFT");
    }
  }
}
