//////////////////////////////////////////////////////////////////
//©2011 bildr
//Released under the MIT License - Please reuse change and share
//Using the easy stepper with your arduino
//use rotate and/or rotateDeg to controll stepper motor
//speed is any number from .01 -> 1 with 1 being fastest - 
//Slower Speed == Stronger movement
/////////////////////////////////////////////////////////////////

#define DIR_PIN 2
#define STEP_PIN 3
#define SPEED .1
int dataIn = 0;

void setup() { 
  pinMode(DIR_PIN, OUTPUT); 
  pinMode(STEP_PIN, OUTPUT); 
  Serial.begin(9600);
} 

void loop(){ 

  //rotate a specific number of degrees 
   if(Serial.available() > 0){ //checks to see if data is available
    dataIn = Serial.read();
    Serial.println(dataIn);
   TypeCheck(dataIn);
   }
//  rotateDeg(720, .2); 
//  delay(2000);
//  rotateDeg(-1440, .2);
//  delay(2000);
//  rotateDeg(720, .2); 
//  delay(2000);
}

void TypeCheck(int dataIn){
  if(dataIn == 48){
    rotateDeg(720, SPEED);
  }
  if(dataIn == 49){
    rotateDeg(-720, SPEED);
  }
}

void rotate(int steps, float speed){ 
  //rotate a specific number of microsteps (8 microsteps per step) - (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (steps > 0)? HIGH:LOW;
  steps = abs(steps);

  digitalWrite(DIR_PIN,dir); 

  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(STEP_PIN, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(STEP_PIN, LOW); 
    delayMicroseconds(usDelay); 
  } 
} 

void rotateDeg(float deg, float speed){ 
  //rotate a specific number of degrees (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (deg > 0)? HIGH:LOW;
  digitalWrite(DIR_PIN,dir); 

  int steps = abs(deg)*(1/0.225);
  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(STEP_PIN, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(STEP_PIN, LOW); 
    delayMicroseconds(usDelay); 
  } 
}
