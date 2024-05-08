#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "WIFI ODC";
const char* password = "Digital1";
const char* serverName = "http://192.168.252.210:8000/save"; // Update with your server endpoint
const char* contentType = "application/json"; // Specify content type

unsigned long lastTime = 0;
unsigned long timerDelay = 5000;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;

      http.begin(client, serverName);

      // Add headers
      http.addHeader("Content-Type", contentType);

      // JSON data to send in the POST request
      String postData = "{\"valeur\":\"bini_jean\"}"; // Update with your JSON data

      // Send HTTP POST request
      int httpResponseCode = http.POST(postData);

      // Print HTTP response code
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);

      // Print response from server
      String response = http.getString();
      Serial.println("Response:");
      Serial.println(response);

      // End HTTP connection
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
}
