#include <WiFi.h>
#include <ESP32_Servo.h>
#include <LiquidCrystal.h>

Servo myservo; 
WiFiServer server(5000);
LiquidCrystal lcd(14, 26, 5, 4, 2, 15);

void setup() {
  lcd.begin(16,2);
  lcd.print("Jai Mata Di");
  delay(500);
  lcd.clear();
  lcd.print("Welcome!");
  delay(1000);
  Serial.begin(19200);
  pinMode(12,OUTPUT);
  pinMode(27,OUTPUT);
  myservo.attach(13);
  WiFi.begin("PESU-Element Block", "");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
  lcd.begin(16,2);
  lcd.clear();
  lcd.print(WiFi.localIP().toString());
  myservo.write(180);
  digitalWrite(12,LOW);
}

void loop() {
 
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Client connected");
    lcd.begin(16,2);
    while (client.connected()) {
      if (client.available()) {
        String message = client.readStringUntil('\n');
        Serial.print("Received message: ");
        Serial.println(message+"\n");
        if (message!="null"){
          myservo.write(0);
          digitalWrite(27,HIGH);
          lcd.clear();
          lcd.print("Welcome " + message);
          delay(7000);
          lcd.clear();
          lcd.print("Scan Now.");
          myservo.write(180);
          digitalWrite(27,LOW);
        }
        else{
          lcd.clear();
          lcd.print("Unrecognized");
          lcd.setCursor(0,1);
          lcd.print("Access");
          digitalWrite(12,HIGH);
          delay(3000);
          lcd.setCursor(0,0);
          lcd.clear();
          
          lcd.print("Scan Again.");
          digitalWrite(12,LOW);
        }
      }
    }
    Serial.println("Client disconnected");
  }
}