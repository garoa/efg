bool flag = false;
int Time1 = 0; //In miliseconds
int Time2 = 0;
int delta_time = 0;


void setup() {
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(7, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(7, LOW);
  Serial.begin(9600);
  flag = false;
}

void loop() {
  //flag = false;
  if (!digitalRead(5)) {
    //flag =true;
    Time1 = millis();
    while (digitalRead(4)) {
      digitalWrite(13,HIGH);
    }
    digitalWrite(13,LOW);
    Time2 = millis();
    delta_time = Time2 - Time1;
    Serial.println(delta_time);
    Serial.println(115*313.2/delta_time);
    Serial.println();
    //flag = false;
    delay(500);
  }
  if (!digitalRead(4)) {
    //flag =true;
    Time1 = millis();
    while (digitalRead(5)) {
      digitalWrite(13,HIGH);
    }
    digitalWrite(13,LOW);
    Time2 = millis();
    delta_time = Time2 - Time1;
    Serial.println(delta_time);
    Serial.println(115*313.2/delta_time);
    Serial.println();
    //flag = false;
    delay(500);
  }
}
