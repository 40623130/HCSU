String readString;

void setup(){
  Serial.begin(115200);
}

void loop(){
  while(!Serial.available()) {
    delay(10);
  }
  while (Serial.available()){
    delay(10);
    if (Serial.available() >0){
      char T = Serial.read();  //gets one byte from serial buffer
      readString += T; //makes the string readString
      if (readString == "Right"){
        Serial.print("RRRRR");
      }
      else if (readString == "2"){
        Serial.print("222");
      }
    }
  }
  if (readString.length() >0){
    Serial.print("Arduino received: ");  
    Serial.println(readString); //see what was received
    readString = "";
  }
}
