int OUT = 2;  //pin 2 Arduino connected to the sensor output
int D = 0, O = 0;
bool guardarestado;
void setup() {
  Serial.begin(9600);   //initiates serial monitor
  pinMode(OUT, INPUT);  // setting pin 2 in Arduino as output
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
}