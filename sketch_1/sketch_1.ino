#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiUdp.h>

const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";
const char* server_ip = "192.168.1.2";  // Replace with your server IP address
const int server_port = 8888;

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
}

void loop() {
    // Collect data (e.g., RSSI)
    int rssi = WiFi.RSSI();

    // Send data to the server
    sendToServer(rssi);

    delay(1000);  // Adjust the delay as needed
}

void sendToServer(int data) {
    WiFiClient client;

    if (client.connect(server_ip, server_port)) {
        client.print(data);
        client.stop();
    }
}