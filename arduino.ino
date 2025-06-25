#include <Servo.h>

Servo xServo;
Servo yServo;
const int relayPin = 7;

void setup() {
  xServo.attach(9);  // X servo
  yServo.attach(10); // Y servo
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);  // Start off

  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\\n');
    command.trim();

    if (command.startsWith("MOVE")) {
      int xIndex = command.indexOf('X');
      int yIndex = command.indexOf('Y');
      int sIndex = command.indexOf("SPRAY");

      int xZone = command.substring(xIndex + 1, yIndex).toInt();
      int yZone = command.substring(yIndex + 1, sIndex).toInt();

      moveToZone(xZone, yZone);
      spray();
    }
  }
}

void moveToZone(int x, int y) {
  int xAngle = map(x, 0, 2, 0, 180);  // 3 zones
  int yAngle = map(y, 0, 2, 0, 180);
  xServo.write(xAngle);
  yServo.write(yAngle);
  delay(1000);
}

void spray() {
  digitalWrite(relayPin, HIGH);
  delay(2000);
  digitalWrite(relayPin, LOW);
}
