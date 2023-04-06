/* Importação de bibliotecas do módulo ESP8266 e Servo Motor*/
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <Servo.h>

/* O BlynkCloud  gerou esse código para fazer a comunicação do circuito com o web ou aplicativo */

#define BLYNK_TEMPLATE_ID "TMPLCICrYx4x"
#define BLYNK_TEMPLATE_NAME "NodeMCU"
#define BLYNK_AUTH_TOKEN "_lDNELJwBKNXaRNC8m_DvMKpX-dD8HQ-"

/* -- Fim código gerado  -- */

/* Autenticação do servidor web + configuração na minha rede wifi */
char auth[] = BLYNK_AUTH_TOKEN; 
char ssid[] = "WANESSA OI FIBRA 2.4G";
char pass[] = "wanejunior";
/* ----------*/

/* Declaração de variáveis dos pinos*/
Servo servo;
int buzzer = D5;
int led = D0;

/* Operação de ligar/desligar led com blynk */
BLYNK_WRITE(V0) {
  digitalWrite(led, param.asInt());
}

/* Escrever o grau em que o servo motor irá girar pelo app ou web*/
BLYNK_WRITE(V1) {
  servo.write(0);
  delay(2000);
  servo.write(param.asInt());
  delay(2000);
}

/* Escrever o valor em hertz do buzzer pelo app ou web*/
BLYNK_WRITE(V2) {
  int value = param.asInt();
  tone(buzzer, value);
}

/* Definição das operações dos pinos se é saída ou entrada*/
void setup() {
  
  pinMode(led, OUTPUT); // Indica que o pino do ESP8266 (D0) da variável (led) será de saída, ou seja, passaremos um valor para esse pino
  pinMode(buzzer, OUTPUT);
  servo.attach(D1); // Atribuindo o pino D1 ao servo motor
  
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80); // Inicializando o Blynk com as configurações de Wifi
  
}

void loop() {
  
  Blynk.run(); // Executando o blynk

}
