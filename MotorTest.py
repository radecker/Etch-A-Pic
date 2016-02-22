import sys
import time
import RPi.GPIO as GPIO
class Motor:
# Use BCM GPIO references
# instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 35, 36, 37, 38, 29, 31, 32, 33, 13, 15, 16, 18
# GPIO19, GPIO16, GPIO26, GPIO20, GPIO5, GPIO6, GPIO12, GPIO13, GPIO27, GPIO22, GPIO23, GPIO24
    StepPins = [19,16,26,20,5,6,12,13,27,22,23,24]

# Set all pins as output
    for pin in StepPins:
        print "Setup pins"
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)

    StepPin1 = 19
    DirPin1 = 16
    StepPin2 = 26
    DirPin2 = 20
    Step = 0.01
    #Dir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

    def rotate(steps, speed, DirPin, StepPin):
        bool dir
        if (steps > 0):
            bool = True
        else:
            bool = False
        steps = abs(steps)
        GPIO.output(DirPin,dir)
        delay = (1/speed) * 70
        
        for i in range(0, steps):
            GPIO.output(StepPin, True)
            time.sleep(delay)
    
    def rotate2(steps1, steps2, speed, DirPin1, StepPin1, DirPin2, StepPin2):
        bool dir
        if (steps1 > 0):
            dir = True
        else:
            dir = False
        if (steps2 > 0):
            dir = True
        else:
            dir = False
        steps1 = abs(steps1)
        steps2 = abs(steps2)
        GPIO.output(DirPin1,dir)
        GPIO.output(DirPin2,dir)
        delay = (1/speed) * 70
        
        for i in range(0, steps1):
            GPIO.output(StepPin1, True)
            GPIO.output(StepPin2, True)
            time.sleep(delay)
    
    
    def rotateDeg(deg, speed, DirPin, StepPin)
        bool dir
        if (steps > 0):
            bool = True
        else:
            bool = False
        int steps = abs(deg)*(1/0.225)
        GPIO.output(DirPin,dir)
        for i in range(0, steps):
            GPIO.output(StepPin, True)
            time.sleep(delay)
        GPIO.output(StepPin, False)
        time.sleep(delay)
    def left(steps, speed)
        rotate(steps, speed, StepPin1, DirPin1) #TODO Change sign of steps, so that it reflects actual movement of motor
        GPIO.output(StepPin, False)
        time.sleep((1/speed) * 70)
    def right(steps, speed)
        rotate(steps, speed, StepPin1, DirPin1) #TODO Change sign of steps, so that it reflects actual movement of motor
        GPIO.output(StepPin, False)
        time.sleep((1/speed) * 70)
    def down(steps, speed)
        rotate(steps, speed, StepPin2, DirPin2) #TODO Change sign of steps, so that it reflects actual movement of motor
        GPIO.output(StepPin, False)
        time.sleep((1/speed) * 70)
    def up(steps, speed)
        rotate(steps, speed, StepPin2, DirPin2) #TODO Change sign of steps, so that it reflects actual movement of motor
        GPIO.output(StepPin, False)
        time.sleep((1/speed) * 70)
    def upLeft(steps1, steps2, speed)
        rotate2(steps1,steps2, speed, StepPin1, DirPin1, StepPin2, DirPin2) #TODO Change sign of steps, so that it reflects actual movement of motor
        GPIO.output(StepPin1, False)
        GPIO.output(StepPin2, False)
        time.sleep((1/speed) * 70)
    def upRight(steps1, steps2, speed)
        rotate2(steps1,steps2, speed, StepPin1, DirPin1, StepPin2, DirPin2) #TODO Change sign of steps, so that it reflects actual movement of motor
        GPIO.output(StepPin1, False)
        GPIO.output(StepPin2, False)
    def downLeft(steps1, steps2, speed)
        rotate2(steps1,steps2, speed, StepPin1, DirPin1, StepPin2, DirPin2) #TODO Change sign of steps, so that it reflects actual movement of motor    
        GPIO.output(StepPin1, False)
        GPIO.output(StepPin2, False)
    def downRight(steps1, steps2, speed)
        rotate2(steps1,steps2, speed, StepPin1, DirPin1, StepPin2, DirPin2) #TODO Change sign of steps, so that it reflects actual movement of motor    
        GPIO.output(StepPin1, False)
        GPIO.output(StepPin2, False)
'''
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# Initialise variables
StepCounter = 0

# Start main loop
while True:

  print StepCounter,
  print Seq[StepCounter]

  for pin in range(0,4):
    xpin=StepPins[pin]# Get GPIO
    if Seq[StepCounter][pin]!=0:
      print " Enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir

  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir

  # Wait before moving on
  time.sleep(WaitTime)
  '''
