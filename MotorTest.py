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

    StepPin = 19
    DirPin = 16
    Step = 0.01
    Dir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

    def rotate(steps, speed):
        bool dir
        if (steps > 0):
            bool = True
        else:
            bool = False
        steps = abs(steps)
        for i in range(0, steps):
            GPIO.output(19, True)



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