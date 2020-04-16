#include <AccelStepper.h>
const int pinSwEnable = 7;  //il bottone presente nel modulo joystick che abilita o disabilita il controllo
const int pinEnable = 8;  //i pin che comandano lo stato ENABLE dei driver A4988 sono in collegati in serie per questo basta un solo pin per gestirli entrambi

unsigned long debounceDelay = 10; //millisecondi per il debonuce del bottone

const int jX = A0;  //pin analogico che legge i valori per le X
const int stepX = 3;  //pin digitale che invia i segnali di STEP al driver delle X
const int dirX = 4; //pin digitale che invia il segnale DIREZIONE al driver delle X
long speedX, valX, mapX;  //variabili di gestione movimenti motore X

const int jY = A1;  //pin analogico che legge i valori per le Y
const int stepY = 5;  //pin digitale che invia i segnali di STEP al driver delle Y
const int dirY = 6; //pin digitale che invia il segnale DIREZIONE al driver delle Y
long speedY, valY, mapY;  //variabili di gestione movimenti motore Y

//variabili utilizzate dalla libreria AccelStepper
const int maxSpeed = 1000;  //stando alla documentazione della libreria questo valore può essere impostato fino a 4000 per un Arduino UNO
const int minSpeed = 0; //velocità minima del motore
const float accelerazione = 50.0; //numero di step al secondo in accelerazione

const int treshold = 30;  //la lettura dei potenziometri non è mai affidabile al 100%, questo valore aiuta a determinare il punto da considerare come "Stai fermo" nei movimenti
long tresholdUp, tresholdDown;  //variabili di servizio per espletare il compito descritto sopra

boolean abilitato, muoviX, muoviY, enable;  //variabili di gestione dei movimenti

Bounce btnEnable = Bounce();  //istanzia un bottone dalla libreria Bounce

//istanzia i motori
AccelStepper motoreX(AccelStepper::DRIVER, stepX, dirX);
AccelStepper motoreY(AccelStepper::DRIVER, stepY, dirY);

void setup() {
  //inizializza valori
  speedX = speedY = 0;
  enable = false;

  //definizione delle modalità dei pin
  pinMode(ledEnable, OUTPUT);
  pinMode(pinEnable, OUTPUT);

  pinMode(pinSwEnable, INPUT_PULLUP); //l'input dello switch ha bisogno di essere settato come INPUT_PULLUP

  digitalWrite(ledEnable, enable);
  digitalWrite(pinEnable, !enable); //I driver A4988 disabilitano i comandi al motore se sul pin ENABLE ricevono un segnale HIGH per questo motivo il valore è opposto a quello del LED

  //configura il bottone del joystick utilizzando la libreria Bounce
  btnEnable.attach(pinSwEnable);
  btnEnable.interval(debounceDelay);

  //calcola range valori entro i quali considerare la posizione del joystick come "Stai fermo"
  tresholdDown = (maxSpeed / 2) - treshold;
  tresholdUp = (maxSpeed / 2) + treshold;

  //configura parametri dei motori
  motoreX.setMaxSpeed(maxSpeed);
  motoreX.setSpeed(minSpeed);
  motoreX.setAcceleration(accelerazione);

  motoreY.setMaxSpeed(maxSpeed);
  motoreY.setSpeed(minSpeed);
  motoreY.setAcceleration(accelerazione);
}

void loop() {

  digitalWrite(ledEnable, enable);  //mostra stato di abilitazione tramite il led su pin 13
  digitalWrite(pinEnable, !enable); //imposta valore opposto sui pin ENABLE dei driver

  //esegui lettura analogica dei valori provenienti dai potenziometri del joystick
  valX = analogRead(jX);
  valY = analogRead(jY);

  //mappa i valori letti in funzione della velocità inima e massima
  mapX = map(valX, 0, 1023, minSpeed, maxSpeed);
  mapY = map(valY, 0, 1023, minSpeed, maxSpeed);

  //esegui funzione di comando dei motori
  pilotaMotori(mapX, mapY);

}

void pilotaMotori(long mapX, long mapY) {

  if (mapX <= tresholdDown) {
    //x va indietro
    speedX = -map(mapX, tresholdDown, minSpeed,   minSpeed, maxSpeed);
    muoviX = true;
  } else if (mapX >= tresholdUp) {
    //x va avanti
    speedX = map(mapX,  maxSpeed, tresholdUp,  maxSpeed, minSpeed);
    muoviX = true;
  } else {
    //x sta fermo
    speedX = 0;
    muoviX = false;
  }

  if (mapY <= tresholdDown) {
    //y va giù
    speedY = -map(mapY, tresholdDown, minSpeed,   minSpeed, maxSpeed);
    muoviY = true;
  } else if (mapY >= tresholdUp) {
    //y va su
    speedY = map(mapY,  maxSpeed, tresholdUp,  maxSpeed, minSpeed);
    muoviY = true;
  } else {
    //y sta fermo
    speedY = 0;
    muoviY = false;
  }

  if (muoviX) {
    motoreX.setSpeed(speedX);
    motoreX.run();
  } else {
    motoreX.stop();
  }

  if (muoviY) {
    motoreY.setSpeed(speedY);
    motoreY.run();
  } else {
    motoreY.stop();
  }
}


void checkEnable() {

  btnEnable.update();

  if (btnEnable.fell()) {
    enable = !enable;
  }

}
