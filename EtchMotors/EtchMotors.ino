
//0.68
//0.59
#define DIR_PIN 2  // Right Motor
#define STEP_PIN 3 // Right Motor
#define DIR_PIN2 4  // Left Motor
#define STEP_PIN2 5  // Left Motor
#define SPEED 2 //2 
int STEPSIZE =  200; // 200
int dataIn = 0;
int LEDPin = 13;


void setup() { 
  pinMode(DIR_PIN, OUTPUT); 
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN2, OUTPUT); 
  pinMode(STEP_PIN2, OUTPUT);
  pinMode(LEDPin, OUTPUT);
  Serial.begin(9600);
} 

void loop(){ 

  //rotate a specific number of degrees 
  
   if(Serial.available() > 0){ //checks to see if data is available
    dataIn = Serial.read();
    Serial.println(dataIn);
   TypeCheck(dataIn);
   //digitalWrite(LEDPin, HIGH);
   //delay(0.00001);
   //digitalWrite(LEDPin, LOW);
   //delay(0.00001);
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
    rotate(-STEPSIZE*.295,SPEED,2); // up limiter
    rotate(STEPSIZE,SPEED,4);
    rotate(STEPSIZE,SPEED,2);
    rotate(-STEPSIZE,SPEED,4);
    rotate(-STEPSIZE,SPEED,2);
  }
  //Down
  if(dataIn == 49){
    rotate(STEPSIZE*.295, SPEED,2);
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
  }
  //Left
  if(dataIn == 50){
    rotate(STEPSIZE*.34,SPEED,4);
    rotate(STEPSIZE,SPEED,4);
    rotate(STEPSIZE,SPEED,2);
    rotate(-STEPSIZE,SPEED,4);
    rotate(-STEPSIZE,SPEED,2);
  }
  //Right
  if(dataIn == 51){
    rotate(-STEPSIZE*.34, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
  }
  if(dataIn == 52){
    //UpRight
    rotate(-STEPSIZE*.67, SPEED,4);  //.34
    rotate(-STEPSIZE*.625, SPEED,2);  //.295
    rotate(STEPSIZE, SPEED,4);
    rotate(STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
  }
  if(dataIn == 53){
    //DownLeft
    rotate(STEPSIZE, SPEED,2);
    rotate(STEPSIZE, SPEED,4);
    rotate(STEPSIZE*.313, SPEED,2); //.295
    rotate(STEPSIZE*.358, SPEED,4); //.34
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
    
  }
  if(dataIn == 54){
    //DownRight
    rotate(STEPSIZE, SPEED,2);
    rotate(-STEPSIZE*.67, SPEED,4);  //.34
    rotate(STEPSIZE*.225, SPEED,2);  //.295
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE, SPEED,2);
    rotate(-STEPSIZE, SPEED,4);
  }
  if(dataIn == 55){
    //UpLeft
    rotate(STEPSIZE, SPEED,4);
    rotate(-STEPSIZE*.225, SPEED,2);  //.295
    rotate(STEPSIZE*.27, SPEED,4);  //.34
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

    //float usDelay = (1/speed) * 70;
    float usDelay = 35; //250

    for(int i=0; i < steps; i++){ 
      digitalWrite(STEP_PIN, HIGH); 
      delayMicroseconds(usDelay); 

      digitalWrite(STEP_PIN, LOW); 
      delayMicroseconds(usDelay); 
    } 
  }
  if(dir_pin == 4) {
    digitalWrite(DIR_PIN2,dir); 

    float usDelay = 35;

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
