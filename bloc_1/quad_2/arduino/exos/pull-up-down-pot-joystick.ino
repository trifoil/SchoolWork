int BTN = 3;
int BTN2 = 4;
int POT = A5;
int JoystickX = A2;
int JoystickY = A1;

int valueBTN;
int valueBTN2;
int valuePOT;
int valueJoystickX;
int valueJoystickY;

int LED = 13;
int LED2 = 12;
 
void setup() {
  Serial.begin(9600);
  pinMode(BTN, INPUT);
  pinMode(BTN2, INPUT);
  pinMode(POT, INPUT);
  pinMode(JoystickX, INPUT);
  pinMode(JoystickY, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  valueBTN = digitalRead(BTN);
  if (valueBTN == HIGH) {
    digitalWrite(LED, LOW);
  } else {
    digitalWrite(LED, HIGH);
  }

  valueBTN2 = digitalRead(BTN2);
  if (valueBTN2 == HIGH) {
    digitalWrite(LED2, HIGH);
  } else {
    digitalWrite(LED2, LOW);
  }

  valuePOT = analogRead(POT);
  Serial.print("POT value: ");
  Serial.print(valuePOT);

  Serial.print(", ");

  valueJoystickX = analogRead(JoystickX);
  Serial.print("X: ");
  Serial.print(valueJoystickX);

  Serial.print(", ");

  valueJoystickY = analogRead(JoystickY);
  Serial.print("Y: ");
  Serial.print(valueJoystickY);

  Serial.println(".");
}