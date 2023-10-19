//Instalar librerias
#include <ESP8266WiFi.h> 
#include <ESP8266HTTPClient.h>

int OUT = 2;  // Pin 2 de Arduino conectado a la salida del sensor
int D = 0, O = 0;
bool guardarestado, estadoanterior = false; 
const char* ssid = "TU_SSID"; 
const char* password = "TU_CONTRASEÑA";
const char* server = "DIRECCION_DEL_SERVIDOR";

void setup() {
  Serial.begin(9600);
  pinMode(OUT, INPUT);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conectado a WiFi");
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
    enviarEstado(guardarestado); //Envia el estado a django para modificarlo
  }
}


void enviarEstado(int sensor_id, bool estado) {
  HTTPClient http;

  String url = "http://localhost:8000/actualizar_estado/";
  
  url += "?id=";
  url += sensor_id;
  url += "&estado=";
  url += (estado ? "1" : "0");

  http.begin(url);
  int httpCode = http.GET();

  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println(payload);
  } else {
    Serial.println("Error en la petición HTTP");
  }

  http.end();
}

