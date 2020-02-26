#define EN 8 
#define X_DIR 5
#define X_STP 2
#define limitPin 9
int stps = 2000;
int state = 1;

void setup() {
  Serial.begin(9600);
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(limitPin, INPUT);
  digitalWrite(EN, LOW);
}

void step(boolean dir, byte dirPin, byte stepperPin, long int stps)
{
  digitalWrite(dirPin, dir);
  delay(100);
  for (long int i = 0; i < stps; i++) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(600);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(600);
    if (digitalRead(limitPin) == HIGH){
      break;
    }
  }
}

void loop() {
  if(digitalRead(limitPin) == LOW){
    switch(state){
      case 0:
        Serial.println("LOW and state=0");
        step(true, X_DIR, X_STP, stps);
        break;
      case 1:
        Serial.println("LOW and state=1");
        step(false, X_DIR, X_STP, stps);
        break;
      default:
        Serial.println("LOW");
    }
  }
  else if(digitalRead(limitPin) == HIGH){
    switch(state){
      case 0:
        Serial.println("HIGH and state=0");
        state = 1;
        break;
      case 1:
        Serial.println("HIGH and state=1");
        state = 0;
        break;
      default:
        Serial.println("HIGH");
    }
  }
}
