//////////////////////////////////////////////////////////////////
//©2011 bildr
//Released under the MIT License - Please reuse change and share
//Using the easy stepper with your arduino
//use rotate and/or rotateDeg to controll stepper motor
//speed is any number from .01 -> 1 with 1 being fastest - 
//Slower Speed == Stronger movement
/////////////////////////////////////////////////////////////////

#define DIR_PIN 2  // Right Motor
#define STEP_PIN 3 // Right Motor
#define DIR_PIN2 4  // Left Motor
#define STEP_PIN2 5  // Left Motor
#define SPEED 2 
int STEPSIZE = 800;
int dataIn = 0;

void setup() { 
  pinMode(DIR_PIN, OUTPUT); 
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN2, OUTPUT); 
  pinMode(STEP_PIN2, OUTPUT); 
  Serial.begin(9600);
} 

void loop(){ 

  //rotate a specific number of degrees 
  
   if(Serial.available() > 0){ //checks to see if data is available
    dataIn = Serial.read();
    Serial.println(dataIn);
   TypeCheck(dataIn);
   }
   
//rotate2(100, false, false, 2);
//delay(20);
//  rotateDeg(720, .2); 
//  delay(2000);
//  rotateDeg(-1440, .2);
//  delay(2000);
//  rotateDeg(720, .2); 
//  delay(2000);
}


void TypeCheck(int dataIn){
  //Up
  if(dataIn == 48){
    rotate(-STEPSIZE*.59,SPEED,2); // up limiter
    rotate(STEPSIZE,SPEED,4);
    rotate(STEPSIZE,SPEED,2);
    rotate(-STEPSIZE,SPEED,4);
    rotate(-STEPSIZE,SPEED,2);
  }
  //Down
  if(dataIn == 49){
    rotate(STEPSIZE*.59, SPEED,2);
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
  }
  //Left
  if(dataIn == 50){
    rotate(STEPSIZE*.68,SPEED,4);
    rotate(STEPSIZE,SPEED,4);
    rotate(STEPSIZE,SPEED,2);
    rotate(-STEPSIZE,SPEED,4);
    rotate(-STEPSIZE,SPEED,2);
  }
  //Right
  if(dataIn == 51){
    rotate(-STEPSIZE*.68, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
  }
  if(dataIn == 52){
    //UpRight
    rotate(-STEPSIZE*.68, SPEED,4);
    rotate(-STEPSIZE*.59, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
  }
  if(dataIn == 53){
    //DownLeft
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
    
  }
  if(dataIn == 54){
    //DownRight
    rotate(STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
  }
  if(dataIn == 55){
    //UpLeft
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
  }
}

void rotate(int steps, float speed,int dir_pin){ 
  //rotate a specific number of microsteps (8 microsteps per step) - (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (steps > 0)? HIGH:LOW;
  steps = abs(steps);
  if(dir_pin == 2) {
    digitalWrite(DIR_PIN,dir); 

    float usDelay = (1/speed) * 70;

    for(int i=0; i < steps; i++){ 
      digitalWrite(STEP_PIN, HIGH); 
      delayMicroseconds(usDelay); 

      digitalWrite(STEP_PIN, LOW); 
      delayMicroseconds(usDelay); 
    } 
  }
  if(dir_pin == 4) {
    digitalWrite(DIR_PIN2,dir); 

    float usDelay = (1/speed) * 70;

    for(int i=0; i < steps; i++){ 
      digitalWrite(STEP_PIN2, HIGH); 
      delayMicroseconds(usDelay); 

      digitalWrite(STEP_PIN2, LOW); 
      delayMicroseconds(usDelay); 
    } 
  }
}

void rotate2(int steps, boolean dir1, boolean dir2, float speed){ 
  //rotate a specific number of microsteps (8 microsteps per step) - (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  
  steps = abs(steps);

  digitalWrite(DIR_PIN,dir1); 
  digitalWrite(DIR_PIN2,dir2);
  
  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(STEP_PIN, HIGH); 
    digitalWrite(STEP_PIN2, HIGH);
    delayMicroseconds(usDelay); 
    
    digitalWrite(STEP_PIN, LOW); 
    digitalWrite(STEP_PIN2, LOW);
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
