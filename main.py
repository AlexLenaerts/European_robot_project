import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import move
import detection

#BACK
pinTrigger_B = 27
pinEcho_B = 4

#LEFT
pinTrigger_L = 17
pinEcho_L = 18

#FRONT
pinTrigger_F = 22
pinEcho_F = 23

#RIGHT
pinTrigger_R = 24
pinEcho_R = 25

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
       move.forwards()
        time.sleep(0.1)
        if detection.isnearobstacle(hownear,pinTrigger_F,pinEcho_F):
            move.stopmotors()
            detection.avoidobstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
