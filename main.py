import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library
from move import *
from detection import *

# Your code to control the robot goes below this line
try:
    # Set trigger to False (Low)
    GPIO.output(pinTrigger_B, False)
    GPIO.output(pinTrigger_F, False)
    GPIO.output(pinTrigger_R, False)
    GPIO.output(pinTrigger_L, False)

    # Allow module to settle
    time.sleep(0.1)
    # repeat the next indented block forever
    while True:
       forwards()
       time.sleep(0.1)
       if isnearobstacle(hownear,pinTrigger_F,pinEcho_F):
            stopmotors()
            avoidobstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
