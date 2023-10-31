#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <WiFiUdp.h>

int OUT = 2;  // Pin 2 de Arduino conectado a la salida del sensor
int D = 0, O = 0,ID=1;
bool guardarestado, estadoanterior = false; 

//UTN #define WIFI_SSID "Utn_Libre Max"  // Nombre de la red a conectarse
//UTN #define WIFI_PASSWORD ""           // Contraseña de la red
#define WIFI_SSID "Personal-E78"  
#define WIFI_PASSWORD "COE2953E78"           
void conectarWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Conectando a Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Conectado con IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  pinMode(OUT, INPUT);
  conectarWiFi();
}

void loop() {
  while (D < 5 && O < 5) {
    if (digitalRead(OUT) == 1) {
      O = 0;
      D++;
    } else {
      D = 0;
      O++;
    }
    delay(500);
  }
  if (D >= 5) {
    guardarestado = false;
    D = 0;
  } else {
    guardarestado = true;
    O = 0;
  }
  Serial.print("Estado:");
  Serial.println(guardarestado);

  if (estadoanterior != guardarestado) {
    estadoanterior = guardarestado;
    enviarEstado(ID,guardarestado); //Envia el estado a django para modificarlo
  }
}

void enviarEstado(int sensor_id, bool estado) {
  WiFiClient client;

  String url = "http://localhost:8000/actualizar_estado/";
  url += "?id=" + String(sensor_id) + "&estado=" + String(estado ? "1" : "0");

  if (client.connect("localhost", 8000)) {
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                 "Host: localhost\r\n" +
                 "Connection: close\r\n\r\n");

    while(client.connected() && !client.available()) delay(1);

    while(client.connected() || client.available()) {
      char c = client.read();
      Serial.write(c);
    }
    client.stop();
  } else {
    Serial.println("Error en la conexión");
  }
}